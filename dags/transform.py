#transform drivers with pandas.
import pandas as pd
#%%
def transformTeams(teamsJson,year):
    print("transforming data >>>")
    teamsDf = pd.DataFrame(teamsJson)
    teamsDf['year'] = year
    print("returning the transformed data >>>")
    return teamsDf