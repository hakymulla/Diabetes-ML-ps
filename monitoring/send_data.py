import json
import uuid
from datetime import datetime
from time import sleep
import pandas as pd

# import pyarrow.parquet as pq
import requests


df = pd.read_csv("../datasets/diabetes_012_health_indicators_BRFSS2015.csv.zip")
df.drop("Diabetes_012",axis=1, inplace=True)
# table = pq.read_table("green_tripdata_2022-01.parquet")
# data = table.to_pylist()


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


# with open("target.csv", 'w') as f_target:
for row in df.to_dict('records'):
    # row['id'] = str(uuid.uuid4())
    # duration = (row['lpep_dropoff_datetime'] - row['lpep_pickup_datetime']).total_seconds() / 60
    # f_target.write(f"{row['id']},{duration}\n")
    resp = requests.post("http://127.0.0.1:9696/predict",
                            headers={"Content-Type": "application/json"},
                            data=json.dumps(row, cls=DateTimeEncoder)).json()

    print(f"prediction: {resp['diabetes_binary']}")
    sleep(1)
