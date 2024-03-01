#%%
from google.cloud import bigquery
from google.oauth2 import service_account
import typing

if typing.TYPE_CHECKING:
    from google.cloud import bigquery
import datetime
import pytz
import pandas as pd
#%%

credentialsFileName = "/home/airflow/gcs/dags/vamseeSAcredentials.json"
credentials = service_account.Credentials.from_service_account_file(
    credentialsFileName)
client = bigquery.Client(credentials=credentials)
#%%
jobConfig = bigquery.LoadJobConfig(
    write_disposition = "WRITE_APPEND",
)
def loadData(df,tableId):
    print("entered the loading function >>>")
    tableId = "f1datawarehouse.f1Test.{}".format(tableId)
    job = client.load_table_from_dataframe(
        df,tableId,jobConfig
    )
    print("loading data into big query >>>")
    job.result()
    print("returning the response >>>")
    return "loaded data"


# %%

"""
import extract
import transform

if __name__ == "__main__":
    json = extract.extractDriversData(2022)
    print(json)
    df = transform.transform(json)
    print(df)
    loadData(df)
"""


# %%
