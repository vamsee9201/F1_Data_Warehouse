#%%
import extract
import transform
import load
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime as dt
#%%
default_args = {
    'retries' : 2,
    'retry_delay' : dt.timedelta(minutes=1),
    'email_on_retry' : False,
    'email_on_failure' : False,
}
dag = DAG(
    'drivers_to_bq',
    default_args=default_args,
    start_date=dt.datetime(2021,2,1),
    schedule=dt.timedelta(days=365),
    catchup=True
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
