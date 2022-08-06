import os
import pickle
import requests
import lightgbm as lgb
import pandas as pd

from flask import Flask, request, jsonify
from pymongo import MongoClient


MODEL_FILE = os.getenv('MODEL_FILE', 'lgbm.txt')

EVIDENTLY_SERVICE_ADDRESS = os.getenv('EVIDENTLY_SERVICE', 'http://127.0.0.1:5000')
MONGODB_ADDRESS = os.getenv("MONGODB_ADDRESS", "mongodb://127.0.0.1:27017")

model = lgb.Booster(model_file='lgbm.txt')

app = Flask('diabetes-prediction')
mongo_client = MongoClient(MONGODB_ADDRESS)
db = mongo_client.get_database('prediction_service')
collection = db.get_collection('data')

def preprocess(dict):
    data = pd.DataFrame.from_dict(dict, orient='index').T
    return data

def predict(features):
    preds = model.predict(features)
    return float(preds[0])

def save_to_db(record, prediction):
    print(f'RECORD:    {record}')
    rec = record.copy()
    rec['prediction'] = prediction
    collection.insert_one(rec)


def send_to_evidently_service(record, prediction):
    rec = record.copy()
    rec['prediction'] = prediction
    requests.post(f"{EVIDENTLY_SERVICE_ADDRESS}/iterate/diabetes", json=[rec])


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    input = request.get_json()
    features = preprocess(input)
    pred = predict(features)

    result = {
	     'diabetes_binary': pred
     }

    save_to_db(input, float(pred))
    send_to_evidently_service(input, float(pred))

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)