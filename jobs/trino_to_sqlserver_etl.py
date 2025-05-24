from pyspark.sql import SparkSession
from pyspark.sql.types import *
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_spark_session():
    """Create and configure a Spark session"""
    import os
    import sys
    
    # Get the Python executable from the current environment
    python_executable = sys.executable
    
    return (SparkSession.builder
            .appName("TrinoToSQLServerETL")
            .config("spark.python.executable", python_executable)
            .config("spark.python.worker.reuse", "true")
            .config("spark.executor.memory", "2g")
            .config("spark.driver.memory", "2g")
            .config("spark.sql.legacy.timeParserPolicy", "LEGACY")
            .config("spark.eventLog.enabled", "true")
            .config("spark.eventLog.dir", "/opt/bitnami/spark/event-logs")
            .getOrCreate())

def extract_from_trino(spark, table_name):
    """Extract data from Trino"""
    logger.info(f"Extracting data from Trino table: {table_name}")
    
    # Read from Trino using JDBC
    trino_df = (spark.read
                .format("jdbc")
                .option("url", "jdbc:trino://trino:8080")
                .option("driver", "io.trino.jdbc.TrinoDriver")
                .option("user", "trino")
                .option("dbtable", table_name)
                .load())
    
    return trino_df

def load_to_sqlserver(df, table_name):
    """Load data into SQL Server"""
    logger.info(f"Loading data into SQL Server table: {table_name}")
    
    # Write to SQL Server using JDBC
    (df.write
     .format("jdbc")
     .option("url", "jdbc:sqlserver://sqlserver2019:1433;databaseName=AdventureWorks")
     .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver")
     .option("dbtable", table_name)
     .option("user", "sa")
     .option("password", "YourStrong!Passw0rd")
     .mode("overwrite")
     .save())

def main():
    """Main ETL process"""
    try:
        # Create Spark session
        spark = create_spark_session()
        logger.info("Created Spark session")

        # Example: Extract from Trino's sales data
        sales_df = extract_from_trino(spark, "sales.sales_data")
        
        # Transform data if needed
        # Add any necessary transformations here
        
        # Load into SQL Server
        load_to_sqlserver(sales_df, "Sales.SalesData")
        
        logger.info("ETL process completed successfully")
        
    except Exception as e:
        logger.error(f"ETL process failed: {str(e)}")
        raise
    finally:
        if 'spark' in locals():
            spark.stop()

if __name__ == "__main__":
    main() 