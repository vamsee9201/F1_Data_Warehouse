#%%
import boto3
import pandas as pd
import requests
import json
#%%
credentials = pd.read_csv("aws_credentials.csv")
# %%
accessKeyId = credentials['Access key ID'].iloc[0]
scretAccessKey = credentials['Secret access key'].iloc[0]
# %%
url = "https://5oo1xx09xb.execute-api.us-east-1.amazonaws.com/default/teams"
headers = {
    "Content-Type": "application/json"
}
data = {
    "year": 2023
}
response = requests.put(url, headers=headers, data=json.dumps(data))
# %%
driversJson = response.json()
driversDf = pd.DataFrame(driversJson)
# %%
