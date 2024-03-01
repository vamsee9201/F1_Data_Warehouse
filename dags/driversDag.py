#%%
import extract
import transform
import load
from airflow import DAG
from airflow.operators.python import PythonOperator
#from airflow.operators.python import PythonVirtualenvOperator
import datetime as dt
from airflow.utils.dates import days_ago
import logging
#%%
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
def run_drivers_etl():
    logging.info("getting drivers data")
    df = extract.extractDriversData(2023)
    logging.info("transforming")
    transform1 = transform.transform(df)
    logging.info("loading data")
    load.loadData(transform1,"driversData")
#%%
t1 = PythonOperator(
    task_id = "run_drivers_etl",
    python_callable=run_drivers_etl,
    dag=dag
)
#%%

