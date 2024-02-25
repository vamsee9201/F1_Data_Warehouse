#%%
import extract
import transform
import load
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime as dt
from airflow.utils.dates import days_ago
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
def run_etl(ds=None):
    #for each day, load the previous day
    df = extract.extractDriversData(dt.datetime.strptime(ds,'%Y-%m-%d').year)
    transform = transform.transform(df)
    load = load.loadData(transform)
#%%
t1 = PythonOperator(
    task_id = "run_etl",
    python_callable=run_etl,
    dag=dag
)
#%%
t1
