import pandas as pd
import os
import mlflow
from flask import Flask, request, jsonify
print(f'VERSION:   {mlflow.__version__}')
os.environ["AWS_PROFILE"] = "hakymulla" 
# TRACKING_SERVER_HOST = "ec2-3-94-180-117.compute-1.amazonaws.com"
# mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:5000")

RUN_ID = 'aabf6c1efd4044ca8b48902eba5fdcb4'
logged_model = f's3://diabetes-mlflow-artifact/4/{RUN_ID}/artifacts/models'
model = mlflow.lightgbm.load_model(logged_model)

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