from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'negar',
    'start_date':datetime(2024, 6, 27, 15, 00)
}

## starting with the DAG
with DAG('stream-dag', schedule='@daily', default_args=default_args):
    
