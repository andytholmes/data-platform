FROM bitnami/spark:3.3.0

# Install curl
USER root
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Create directories for data and jars
RUN mkdir -p /opt/bitnami/spark/data/input /opt/bitnami/spark/data/output /opt/bitnami/spark/jars

# Download JDBC drivers
RUN curl -L https://repo1.maven.org/maven2/io/trino/trino-jdbc/412/trino-jdbc-412.jar -o /opt/bitnami/spark/jars/trino-jdbc.jar && \
    curl -L https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/12.4.0.jre11/mssql-jdbc-12.4.0.jre11.jar -o /opt/bitnami/spark/jars/mssql-jdbc.jar

# Copy jobs
COPY jobs/ /opt/bitnami/spark/jobs/

USER 1001 