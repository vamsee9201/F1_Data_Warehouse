# this file will have all the utilities required for big query.
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

credentialsFileName = "vamseeSAcredentials.json" #if you want to use this file independently. replace the credentials file. 
credentials = service_account.Credentials.from_service_account_file(
    credentialsFileName)
client = bigquery.Client(credentials=credentials)
#%%
tableId = "f1datawarehouse.f1Test.driversData"
jobConfig = bigquery.LoadJobConfig(
    write_disposition = "WRITE_APPEND",
)
def loadData(df):
    job = client.load_table_from_dataframe(
        df,tableId,jobConfig
    )
    job.result()
    return "loaded data"

# %%

#function to get data from big query
def getData(sql):
    df = pd.DataFrame()
    return df