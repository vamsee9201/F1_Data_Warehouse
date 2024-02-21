#%%
import boto3
import pandas as pd
#%%
credentials = pd.read_csv("aws_credentials.csv")
# %%
accessKeyId = credentials['Access key ID'].iloc[0]
scretAccessKey = credentials['Secret access key'].iloc[0]
# %%
