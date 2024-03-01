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
    'teams_to_bq',
    default_args=default_args,
    schedule_interval='@once',
    start_date=days_ago(1),
    
)
def run_teams_etl():
    logging.info("getting drivers data")
    df = extract.extractTeamsData(2023)
    logging.info("transforming")
    transform1 = transform.transform(df)
    logging.info("loading data")
    load.loadData(transform1)
#%%
t1 = PythonOperator(
    task_id = "run_teams_etl",
    python_callable=run_teams_etl,
    dag=dag
)
#%%

