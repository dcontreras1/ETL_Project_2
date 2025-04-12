from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from Extract import extract
from Transform import transform
from merge_data_API import merge
from Load import load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 1),
    'email': ['d.contreras_d@uao.edu.co'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    'ETL_economy_pipeline',
    default_args=default_args,
    description='ETL DAG for Global Economy Indicators',
    schedule_interval='@daily',
    catchup=False,
    tags=['ETL', 'economy']
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag
)

merge_task = PythonOperator(
    task_id='merge',
    python_callable=merge,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag
)

extract_task >> transform_task >> merge_task >> load_task