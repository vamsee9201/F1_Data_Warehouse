import pandas as pd
import requests
import json
url = "https://5oo1xx09xb.execute-api.us-east-1.amazonaws.com/default/teams"
headers = {
    "Content-Type": "application/json"
}
data = {
         "year": 2014
    }
def extractDriversData(year):
    data['year'] = year
    url = "https://5oo1xx09xb.execute-api.us-east-1.amazonaws.com/default/drivers"
    response = requests.put(url, headers=headers, data=json.dumps(data))
    driversJson = response.json()
    return driversJson

def extractTeamsData(year):
    data['year'] = year
    url = "https://5oo1xx09xb.execute-api.us-east-1.amazonaws.com/default/teams"
    response = requests.put(url, headers=headers, data=json.dumps(data))
    driversJson = response.json()
    return driversJson
