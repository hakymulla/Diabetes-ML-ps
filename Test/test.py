import requests

dataset = {'HighBP': 1.0,
            'HighChol': 0.0,
            'CholCheck': 1.0,
            'BMI': 26.0,
            'Smoker': 0.0,
            'Stroke': 0.0,
            'HeartDiseaseorAttack': 0.0,
            'PhysActivity': 1.0,
            'Fruits': 0.0,
            'Veggies': 1.0,
            'HvyAlcoholConsump': 0.0,
            'AnyHealthcare': 1.0,
            'NoDocbcCost': 0.0,
            'GenHlth': 3.0,
            'MentHlth': 5.0,
            'PhysHlth': 30.0,
            'DiffWalk': 0.0,
            'Sex': 1.0,
            'Age': 4.0,
            'Education': 6.0,
            'Income': 8.0
     }

# dataset_cleaned = predict.preprocess(dataset)
# pred = predict.predict(dataset_cleaned)
# print(pred)

url = 'http://localhost:9696/predict'
response = requests.post(url, json=dataset)
print(response.json())