#%%
import extract
import transform
import load
from airflow import DAG
from datetime import datetime
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
    'drivers_to_bq_2',
    default_args=default_args,
    schedule_interval='@yearly',
    start_date=datetime(2024,12,15),
    catchup=False
    
)
def run_etl(year , **kwargs):
    logging.info("getting drivers data")
    df = extract.extractDriversData(year)
    logging.info("transforming")
    transform1 = transform.transform(df)
    logging.info("loading data")
    load.loadData(transform1)
#%%
t1 = PythonOperator(
    task_id = "run_etl_2",
    python_callable=run_etl,
    op_kwargs={'year': '{{ execution_date.year }}'},
    provide_context=True,
    dag=dag
)
#%%

