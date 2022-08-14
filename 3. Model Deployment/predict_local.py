## This file loads model locally

import pandas as pd
import lightgbm as lgb
from flask import Flask, request, jsonify

model = lgb.Booster(model_file='model.lgb')

def preprocess(input_dict):
    """
    Preprocess incoming dataset
    """
    data = pd.DataFrame.from_dict(input_dict, orient='index').T
    return data

def predict(features):
    """
    Predict function
    """
    preds = model.predict(features)
    return float(preds[0])


app = Flask('diabetes-prediction')
@app.route('/predict', methods=['POST'])
def predict_endpoint():
    """
    Full predict workflow and endpoint
    """
    input_json = request.get_json()
    features = preprocess(input_json)
    pred = predict(features)

    result = {
	     'diabetes_binary': pred
     }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)