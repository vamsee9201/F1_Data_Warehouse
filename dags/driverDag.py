#%%
import extract
import transform
import load
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime as dt
from airflow.utils.dates import days_ago
import logging
#%%
#logger = logging.getLogger(__name__)

default_args = {
    'retries' : 2,
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
dag = DAG(
    'drivers_to_bq',
    default_args=default_args,
    schedule_interval='@once',
    start_date=days_ago(1),
    
)
def run_etl():
    #for each day, load the previous day
    #for each day, load the previous day
    logging.info("getting drivers data")
    df = extract.extractDriversData(2023)
    logging.info("transforming")
    transform1 = transform.transform(df)
    logging.info("loading data")
    load.loadData(transform1)
#%%
t1 = PythonOperator(
    task_id = "run_etl",
    python_callable=run_etl,
    dag=dag
)
#%%
t1
