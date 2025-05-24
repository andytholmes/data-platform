from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_etl',
    default_args=default_args,
    description='Example ETL pipeline using PySpark',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

run_etl = BashOperator(
    task_id='run_etl',
    bash_command='spark-submit --master spark://spark:7077 /opt/bitnami/spark/jobs/etl_job.py',
    dag=dag,
)

run_etl 