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
    print("this is the extract >>>")
    print("year >>>", year)
    data['year'] = year
    print("printing data >>> ",data)
    print("getting response >>>")
    url = "https://5oo1xx09xb.execute-api.us-east-1.amazonaws.com/default/drivers"
    try :
        response = requests.put(url, headers=headers, data=json.dumps(data), timeout=30)
    except Exception as e :
        print("exception created >>>>", e)
    print("getting driversJson data >>>")
    driversJson = response.json()
    print("returning JSON data >>>")
    return driversJson

def extractTeamsData(year):
    print("this is the extract >>>")
    print("year >>>", year)
    data['year'] = year
    print("printing data >>> ",data)
    print("getting response >>>")
    url = "https://5oo1xx09xb.execute-api.us-east-1.amazonaws.com/default/teams"
    try :
        response = requests.put(url, headers=headers, data=json.dumps(data), timeout=30)
    except Exception as e :
        print("exception created >>>>", e)
    print("getting driversJson data >>>")
    teamsJson = response.json()
    print("returning JSON data >>>")
    return teamsJson

# Extracting raw data from the site directly

def extractRaceEventData(year):
    return 0
