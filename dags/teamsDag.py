#%%
import extract
import transform
import load
from airflow import DAG
from airflow.operators.python import PythonOperator
#from airflow.operators.python import PythonVirtualenvOperator
import datetime as dt
from airflow.utils.dates import days_ago
from datetime import datetime
import logging
#%%
default_args = {
    'retries' : 2,
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'schedule_interval':'@yearly',
    'start_date':datetime(2014,12,15)
}
dag = DAG(
    'teams_to_bq',
    default_args=default_args,
    catchup=True
)
def run_teams_etl(**context):
    logging.info("getting drivers data")
    df = extract.extractTeamsData(context['execution_date'].year)
    logging.info("transforming")
    transform1 = transform.transform(df)
    logging.info("loading data")
    load.loadData(transform1,"teamsData")
#%%
t1 = PythonOperator(
    task_id = "run_teams_etl",
    python_callable=run_teams_etl,
    provide_context=True,
    dag=dag
)
#%%

