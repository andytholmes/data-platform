FROM apache/airflow:2.8.0-python3.9

USER root

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Set environment variables
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
ENV AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=False
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_SCHEMA=public
ENV AIRFLOW__WEBSERVER__SECRET_KEY=your_secret_key_here
ENV AIRFLOW__CORE__FERNET_KEY=your_fernet_key_here 