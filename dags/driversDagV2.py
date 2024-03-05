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
from datetime import datetime
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
    catchup=True,
    start_date=datetime(2013,12,14),
    schedule_interval='0 0 15 12 *'
    
)
def run_drivers_etl(**context):
    logging.info("getting drivers data")
    year = context['execution_date'].year + 1
    df = extract.extractDriversData(year)
    logging.info("transforming")
    transform1 = transform.transformDrivers(df)
    logging.info("loading data")
    load.loadData(transform1,"driversData")
#%%
t1 = PythonOperator(
    task_id = "run_drivers_etl",
    python_callable=run_drivers_etl,
    dag=dag
)
#%%

