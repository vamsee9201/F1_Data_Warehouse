#%%
from google.cloud import bigquery
from google.oauth2 import service_account

credentialsFileName = "vamseeSAcredentials.json"
credentials = service_account.Credentials.from_service_account_file(
    credentialsFileName)
client = bigquery.Client(credentials=credentials)
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
# %%
