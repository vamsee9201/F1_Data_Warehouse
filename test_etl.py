#%%
import extract
import transform
import load
import logging
#%%
logger = logging.getLogger(__name__)
#%%
def run_etl():
    #for each day, load the previous day
    logger.info("getting drivers data")
    df = extract.extractDriversData(2023)
    logger.info("transforming")
    transform1 = transform.transform(df)
    logger.info("loading data")
    load.loadData(transform1)
#%%
run_etl()
# %%
