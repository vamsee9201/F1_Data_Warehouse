#transform drivers with pandas.
import pandas as pd
#%%
def transform(driversJson):
    print("transforming data >>>")
    driversDf = pd.DataFrame(driversJson)
    print("returning the transformed data >>>")
    return driversDf