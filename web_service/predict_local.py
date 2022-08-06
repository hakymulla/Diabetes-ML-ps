## This file loads model locally

import pandas as pd
import os
import lightgbm as lgb
from flask import Flask, request, jsonify

model = lgb.Booster(model_file='../models/model.lgb')

def preprocess(dict):
    data = pd.DataFrame.from_dict(dict, orient='index').T
    return data

def predict(features):
    preds = model.predict(features)
    return float(preds[0])


app = Flask('diabetes-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    input = request.get_json()
    features = preprocess(input)
    pred = predict(features)

    result = {
	     'diabetes_binary': pred
     }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)