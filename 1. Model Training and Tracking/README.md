# Model Training and Tracking

## Setup includes setting up an EC2 instance, RDS database and S3 bucket.

## Both experiment tracking and model registry are done in AWS through Jupyter Notebook.

## MLflow was used for Model Experimenting and the best nodel was save in an S3 bucket and alos registered with MLflow.

## How to run on aws
    - Set up an EC2 instance and install appropriate libraries (Conda is sufficient and MLflow)
    - Set up RDS database
    - Set up S3 bucket
    - Set up AWS credentials
    - Change AWS_PROFILE variable with yur AWS credential
    - Change TRACKING_SERVER_HOST variable to public DNS of the EC2 instance
    - Connect to your EC2 instance and Run your Mlflow Server with ---> mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri (database_type)://(username):(password)@(database_address):(port)/database_name --default-artifact-root s3://(S3_bucket_name)
