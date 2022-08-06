# Model Deployment

## Model Deployment as a web service

## How to run 

### test with model saved locally in the models directory
    - pipenv install (to install the libraries in pip file)
    - python3 predict_local.py starts the server
    - python3 test.py to test the model

### test with model saved on AWS S3 bucket 
    - pip install -p (to install the libraries in pip file)
    - python3 predict_remote.py starts the server
    - python3 test.py to test the model

### Test with docker with model saved locally 
    - docker build -t diabetes-prediction-service:v1 .
    - docker run -it --rm -p 9696:9696  diabetes-prediction-service:v1

