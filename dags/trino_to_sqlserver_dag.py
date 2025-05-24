from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'trino_to_sqlserver_etl',
    default_args=default_args,
    description='ETL process to load data from Trino to SQL Server',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
    tags=['etl', 'trino', 'sqlserver'],
)

# Define the Spark job
spark_job = SparkSubmitOperator(
    task_id='trino_to_sqlserver_etl',
    application='/opt/spark/jobs/trino_to_sqlserver_etl.py',
    conn_id='spark_default',
    verbose=True,
    dag=dag,
)

# Set task dependencies
spark_job 