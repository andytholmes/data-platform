# Data Platform

A modern data platform built with Airflow, Spark, SQL Server, Trino, and Jupyter.

## Architecture

```mermaid
graph TB
    subgraph Docker Environment
        subgraph AirflowServices[Airflow Services]
            AirflowInit[Airflow Init<br/>Database & User Setup]
            AirflowWeb[Airflow Webserver<br/>UI & API Interface]
            AirflowSched[Airflow Scheduler<br/>Task Orchestration]
        end
        subgraph SparkCluster[Spark Cluster]
            SparkMaster[Spark Master<br/>Resource Management]
            SparkWorker[Spark Worker<br/>Task Execution]
            SparkHistoryServer[Spark History Server<br/>View Completed Applications]
        end
        SQL[SQL Server 2019<br/>Relational Database]
        Trino[Trino<br/>Distributed SQL Engine]
        Jupyter[Jupyter Notebook<br/>Development Environment]
        Postgres[PostgreSQL 13<br/>Airflow Metadata]
    end

    subgraph Host Access
        Host[Host Machine]
    end

    %% Data Flow
    AirflowInit -->|Initialize DB| Postgres
    AirflowInit -->|Create Admin User| AirflowWeb
    AirflowWeb -->|Orchestrates| SparkMaster
    AirflowWeb -->|Queries| SQL
    AirflowWeb -->|Queries| Trino
    AirflowWeb -->|Metadata| Postgres
    AirflowSched -->|Task Scheduling| AirflowWeb
    SparkMaster -->|Distributes Tasks| SparkWorker
    SparkMaster -->|Event Logs| SparkHistoryServer
    SparkWorker -->|Reads/Writes| Data[(Data Lake)]
    Trino -->|Queries| SQL
    Trino -->|Reads| Data
    Jupyter -->|Development| SparkMaster
    Jupyter -->|Queries| SQL
    Jupyter -->|Queries| Trino

    %% External Access
    AirflowWeb -- "Port 8081<br/>Web UI" --> Host
    Jupyter -- "Port 8888<br/>Notebook UI" --> Host
    Trino -- "Port 8082<br/>Web UI" --> Host
    SQL -- "Port 1433<br/>SQL Queries" --> Host
    SparkMaster -- "Port 7077<br/>Master UI" --> Host
    SparkMaster -- "Port 8080<br/>Application UI" --> Host
    SparkHistoryServer -- "Port 18080<br/>History UI" --> Host

    %% Styling
    classDef docker fill:#2d2d2d,stroke:#00ff00,stroke-width:2px,color:#ffffff
    classDef host fill:#1a1a1a,stroke:#00ff00,stroke-width:2px,color:#ffffff
    classDef data fill:#4d4d4d,stroke:#00ff00,stroke-width:2px,color:#ffffff
    classDef airflow fill:#2d2d2d,stroke:#0066ff,stroke-width:2px,color:#ffffff
    classDef spark fill:#2d2d2d,stroke:#ff9900,stroke-width:2px,color:#ffffff
    class AirflowInit,AirflowWeb,AirflowSched,SparkMaster,SparkWorker,SparkHistoryServer,SQL,Trino,Jupyter,Postgres docker
    class Host host
    class Data data
    class AirflowServices airflow
    class SparkCluster spark
```

## Services

The platform consists of the following services:

- **Airflow**: Orchestrates ETL pipelines using LocalExecutor
  - **Airflow Init**: Initializes the database and creates admin user
  - **Airflow Webserver**: Provides the web interface and API
  - **Airflow Scheduler**: Manages task scheduling and execution
- **Spark**: Processes data using PySpark 3.3
  - **Spark Master**: Manages resources and coordinates tasks
  - **Spark Worker**: Executes tasks and processes data
- **SQL Server**: Provides relational database capabilities
- **Trino**: Distributed SQL query engine
- **Jupyter**: Interactive development environment
- **PostgreSQL**: Metadata database for Airflow

## Prerequisites

- Docker Desktop
- Git
- Conda (Miniconda or Anaconda)
- At least 8GB RAM
- 20GB free disk space

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd data-platform
```

### 2. Set Up Development Environment
```bash
# Create and activate conda environment
./setup_env.sh
conda activate data-platform
```

### 3. Start the Services
```bash
docker compose up --build
```

## Accessing the Services

### Airflow UI
- URL: http://localhost:8081
- Credentials:
  - Username: airflow
  - Password: airflow

### Trino UI
- URL: http://localhost:8082
- No authentication required

### Jupyter Notebook
- URL: http://localhost:8888
- Password: jupyter
- The Jupyter service uses the official `jupyter/datascience-notebook` image without additional dependencies.

### SQL Server
- Host: localhost
- Port: 1433
- Credentials:
  - Username: sa
  - Password: YourStrong!Passw0rd

### Spark UI
- Master UI: http://localhost:7077
- Application UI: http://localhost:8080

### Spark History Server
- URL: http://localhost:18080
- Purpose: The Spark History Server provides a web UI to view completed Spark applications, their event logs, and job details. It is useful for debugging, performance analysis, and auditing past Spark jobs.
- Event Logs Directory: `/opt/bitnami/spark/event-logs` (inside the container)
- The event logs are shared between the Spark containers and the History Server via a Docker volume.
- If you do not see completed applications:
  - Ensure your Spark jobs are configured to enable event logging and write to the correct directory.
  - Check that the event log files exist in the shared directory.
  - Review the History Server container logs for errors.
  - Confirm the volume mount in `docker-compose.yml` is correct.

## Development Workflow

### Running Tests
```bash
# Make sure you're in the conda environment
conda activate data-platform

# Run tests
pytest tests/
```

### Adding New DAGs
1. Create a new Python file in the `dags/` directory
2. Define your DAG using the Airflow Python API
3. The DAG will be automatically picked up by Airflow

### Working with Jupyter
1. Access Jupyter at http://localhost:8888
2. Use the token specified in docker-compose.yml
3. Create new notebooks in the `notebooks/` directory

### Adding Dependencies
1. Add new Python packages to `environment.yml`
2. Update the environment:
```bash
conda env update -f environment.yml
```

## Project Structure

```
data-platform/
├── dags/              # Airflow DAGs
├── jobs/              # Spark jobs
├── tests/             # Unit tests
├── data/              # Data files
├── notebooks/         # Jupyter notebooks
├── docker/            # Docker configurations
│   ├── airflow/      # Airflow Dockerfile
│   ├── spark/        # Spark Dockerfile
│   └── sqlserver/    # SQL Server Dockerfile
├── trino/            # Trino configuration
├── sqlserver/        # SQL Server data
├── environment.yml   # Conda environment
├── setup_env.sh      # Environment setup script
├── docker-compose.yml
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 