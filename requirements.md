# Project Requirements

## Core Dependencies

### Python Environment
- Python 3.9
- Conda (Miniconda or Anaconda)

### Data Processing
- PySpark 3.3.0
- pandas
- numpy

### Database & Data Warehousing
- Apache Airflow 2.8.0
- Trino 0.334.0
- SQL Server 2019
- PostgreSQL

### Development Tools
- Jupyter
- pytest

## Airflow Providers
- apache-airflow-providers-apache-spark==4.11.3
- apache-airflow-providers-microsoft-mssql==3.9.2
- apache-airflow-providers-postgres==5.14.0

## Database Drivers
- pymssql==2.3.4
- sqlalchemy==1.4.54
- psycopg2-binary==2.9.10

## Environment Setup
1. Create conda environment:
   ```bash
   conda env create -f environment.yml
   ```

2. Activate environment:
   ```bash
   conda activate data-platform
   ```

3. Verify installation:
   ```bash
   python -c "import pyspark; print(pyspark.__version__)"
   ```

## System Requirements
- Docker and Docker Compose
- 8GB RAM minimum
- 20GB free disk space
- Network access to required ports (8080, 7077, 1433, etc.)

PySpark + Airflow ETL — Local (Docker Desktop) Requirements

1  Purpose

Provide a fully containerised, test‑driven environment that lets developers run a sample PySpark ETL pipeline orchestrated by Apache Airflow on a single machine using Docker Desktop.

2  Goals & Success Criteria

 ID 

 Goal 

 Success Metric 

 G1

 Spin‑up with one command (docker compose up --build) 

 All services healthy within 2 min 

 G2

 Run example ETL DAG end‑to‑end 

 output/ folder populated with cleaned data 

 G3

 Execute unit tests locally & in CI 

 pytest exit‑code 0, <60 s 

 G4

 Offline‑friendly 

 Only public Docker images & local code; no cloud account needed 

3  In‑Scope Components

Airflow 2.8 – webserver & scheduler (LocalExecutor)

PySpark 3.3 – runs inside a Spark container

Docker Compose v3.8 definitions for Airflow, Spark, and optional services (MinIO for S3 emulation)

Sample ETL job (jobs/etl_job.py) – JSON‑in → JSON‑out, basic cleansing

Airflow DAG (dags/etl_dag.py) – single task calling spark-submit

Unit tests (tests/test_etl.py) – Spark session & transformation logic

Shared volumes for code, data & logs

4  Out‑of‑Scope

Cloud deployment (EKS, GKE, EMR, etc.)

Production‑grade security hardening

External orchestration executors (Celery, KubernetesExecutor)

5  System Context & Data Flow

flowchart TD
    subgraph Docker Desktop
        A[Airflow Webserver] <--volume: dags/jobs--> C(Code Volume)
        S[Airflow Scheduler] <--volume: dags/jobs--> C
        A -->|REST API & UI| B((Browser))
        S -->|spark‑submit| SP[Spark Container]
        SP -->|read input.json| D1[/input data/]
        SP -->|write output/| D2[/output data/]
    end

6  Functional Requirements

 FR 

 Description 

 FR‑1 

 The system shall build all images via docker compose build without external network calls beyond the Docker registry. 

 FR‑2 

 The system shall expose Airflow UI on localhost:8080. 

 FR‑3 

 The Airflow scheduler shall trigger spark-submit inside the Spark container using the shared code volume. 

 FR‑4 

 The ETL job shall drop rows containing NULL values in any column. 

 FR‑5 

 Processed data shall be written to /output as newline‑delimited JSON. 

 FR‑6 

 Unit tests shall execute via pytest inside the Airflow image. 

7  Non‑Functional Requirements

 NFR 

 Requirement 

 NFR‑1 

 Startup time ≤ 2 minutes on a laptop with 8 GB RAM. 

 NFR‑2 

 CPU usage during idle Airflow < 5 %. 

 NFR‑3 

 Images must be reproducible; pinned tags/hashes only. 

 NFR‑4 

 Source code and tests covered by ≥ 80 % statement coverage. 

8  Directory Layout

├── dags/                # Airflow DAGs
├── jobs/                # PySpark ETL scripts
├── tests/               # Pytest suites
├── docker/
│   ├── airflow/
│   │   └── Dockerfile
│   └── spark/
│       └── Dockerfile
├── docker-compose.yml
├── requirements.txt     # Python libs for tests
└── README.md

9  Key Configuration Values

 Item 

 Value / File 

 Airflow executor 

 LocalExecutor (AIRFLOW__CORE__EXECUTOR) 

 Spark image tag 

 bitnami/spark:3.3.0 

 Python base 

 apache/airflow:2.8.0-python3.9 

 Network 

 Compose default bridge 

 Volumes 

 ./dags, ./jobs, ./tests mapped read‑write 

10  Acceptance Tests

Build — docker compose up --build completes without error.

Web UI — Navigate to localhost:8080 and confirm DAG example_etl appears.

Run DAG — Trigger DAG; verify task success & output file exists.

Unit Tests — docker exec airflow pytest returns exit code 0.

Data Correctness — Output JSON has no null values.

11  Future Enhancements (Backlog)

Parameterise input/output paths via Airflow variables.

Add MinIO service & switch ETL to S3‑style URIs.

Replace LocalExecutor with KubernetesExecutor.

Add log aggregation to Prometheus + Grafana.

Revision Date: 20 May 2025