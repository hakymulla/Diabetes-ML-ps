# Lib & Dependencies

import pandas as pd
import numpy as np
import mlflow
import os
import scipy as sp
import gc
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import KFold
import lightgbm as lgb
from prefect import flow
from prefect.task_runners import SequentialTaskRunner

os.environ["AWS_PROFILE"] = "hakymulla" 
RANDOM_STATE = 1111
FOLDS = 5
TRACKING_SERVER_HOST = "ec2-3-94-180-117.compute-1.amazonaws.com"


@flow
def prepare_data(train_path):
    df = pd.read_csv(train_path)
    print(df.shape)
    df.rename(columns={"Diabetes_012":"Diabetes_binary"}, inplace=True)
    train = df.drop('Diabetes_binary', axis=1)
    target = df.loc[:, "Diabetes_binary"]
    print(f"Train shape: {train.shape} and Target shape: {target.shape}")

    return train, target

@flow
def train_best_model(train, target):
    with mlflow.start_run():

        best_params = {'learning_rate':'0.10552983694225122',
                    'max_depth':'89',
                    'min_child_weight':'1.704681566723118',
                    'reg_alpha':'0.010202520050703611',
                    'reg_lambda':'0.046206444839271325',
                    'seed':'42'
                        }

        mlflow.set_experiment("diabetes_")
        mlflow.set_tag("Developer", "Hakymulla")
        mlflow.log_param("Train Data", "datasets/diabetes_binary_5050split_health_indicators_BRFSS2015.csv.zip")
        mlflow.log_param("RANDOM_STATE", RANDOM_STATE)
        mlflow.log_param("FOLDS", FOLDS)
        mlflow.log_params(best_params)
        mlflow.log_param("Models", "LightGBM")

        train_df = train.copy()
        target = target.copy()

        print("Starting Training. Train shape: {}".format(train_df.shape))
        gc.collect()

    #     Cross validation model
        folds = KFold(n_splits= FOLDS, shuffle=True, random_state=RANDOM_STATE)
        
        oof_preds = np.zeros(train_df.shape[0])
        for n_fold, (train_idx, valid_idx) in enumerate(folds.split(train_df, target)):    
            train_x, train_y = train_df.iloc[train_idx], target.iloc[train_idx]
            valid_x, valid_y = train_df.iloc[valid_idx], target.iloc[valid_idx]

            train = lgb.Dataset(train_x, label=train_y)
            valid = lgb.Dataset(valid_x, label=valid_y)

            booster = lgb.train(
            params=best_params,
            train_set=train,
            num_boost_round=1000,
            valid_sets=valid,
            early_stopping_rounds=50
            )

            y_pred = booster.predict(valid_x, raw_score=False)
            y_pred = np.round(y_pred)
            oof_preds[valid_idx] = y_pred

            f_score = f1_score(valid_y, oof_preds[valid_idx])
            accuracy = accuracy_score(valid_y, oof_preds[valid_idx])

            print(f'---------> Fold {n_fold + 1} {f_score}')

            del booster, train_x, train_y, valid_x, valid_y
            gc.collect()

        full_score = f1_score(target, oof_preds)
        full_accuracy_score = accuracy_score(target, oof_preds)

        mlflow.log_metric("f1_score", full_score)
        mlflow.log_metric("accuracy", full_accuracy_score)


        train = lgb.Dataset(train_df, label=target)
        booster = lgb.train(
            params=best_params,
            train_set=train,
            num_boost_round=1000
            )

        booster.save_model('lgbm.txt')
        
        mlflow.lightgbm.log_model(booster, artifact_path="models")
        print(f"default artifacts URI: '{mlflow.get_artifact_uri()}'")

@flow(task_runner=SequentialTaskRunner())
def main(train_path="../datasets/diabetes_binary_5050split_health_indicators_BRFSS2015.csv.zip"):
    # mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:5000")
    mlflow.set_tracking_uri("sqlite:///diabetes_mlflow.db")
    mlflow.set_experiment("diabetes_experiment")
    train, target = prepare_data(train_path).result()
    train_best_model(train, target)

from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import IntervalSchedule
from prefect.flow_runners import SubprocessFlowRunner
from datetime import timedelta

DeploymentSpec(
    flow=main,
    name="model_training",
    schedule=IntervalSchedule(interval=timedelta(minutes=5)),
    flow_runner=SubprocessFlowRunner(),
    tags=["machine_learning"]
)