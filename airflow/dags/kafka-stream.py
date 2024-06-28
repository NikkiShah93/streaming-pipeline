from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'negar',
    'start_date':datetime(2024, 6, 27, 15, 00)
}

def print_welcome():
    print('Welcome to the streaming dag')
def get_data():
    import requests
    res = requests.get('https://randomuser.me/api/')
    res = res.json()
    res = res.get('results', {})
    return res

## starting with the DAG
dag = DAG('stream-dag', schedule='@daily', default_args=default_args)

t1 = PythonOperator('welcome-_log', python_callable=print_welcome, dag=dag)
t2 = PythonOperator('get_data', python_callable=get_data, dag=dag)

## defining the dependencies
t1 >> t2

t1