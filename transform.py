#transform drivers with pandas.
import pandas as pd
#%%
def transform(driversJson):
    driversDf = pd.DataFrame(driversJson)
    return driversDf