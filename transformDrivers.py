#transform drivers with pandas.
import pandas as pd
#%%
def transformDrivers(driversJson):
    driversDf = pd.DataFrame(driversJson)
    return driversDf