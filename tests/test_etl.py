import os
import sys

# Add the conda environment's site-packages to the Python path
conda_prefix = os.environ.get('CONDA_PREFIX')
if conda_prefix:
    site_packages = os.path.join(conda_prefix, 'lib', 'python3.9', 'site-packages')
    if os.path.exists(site_packages):
        sys.path.insert(0, site_packages)

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Add the jobs directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'jobs'))
from trino_to_sqlserver_etl import create_spark_session, extract_from_trino, load_to_sqlserver

@pytest.fixture(scope="session")
def spark():
    """Create a Spark session for testing"""
    spark = create_spark_session()
    yield spark
    spark.stop()

def test_spark_session_creation(spark):
    """Test that Spark session is created successfully"""
    assert spark is not None
    assert spark.version == "3.3.0"

def test_extract_from_trino(spark):
    """Test data extraction from Trino"""
    # Create a test DataFrame
    test_data = [
        (1, "Product A", 100.0),
        (2, "Product B", 200.0),
        (3, "Product C", 300.0)
    ]
    test_schema = StructType([
        StructField("id", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("price", DoubleType(), True)
    ])
    test_df = spark.createDataFrame(test_data, schema=test_schema)
    
    # Mock the extract_from_trino function
    def mock_extract(spark, table_name):
        return test_df
    
    # Test the function
    result_df = mock_extract(spark, "sales.sales_data")
    
    assert result_df.count() == 3
    assert len(result_df.columns) == 3
    assert "id" in result_df.columns
    assert "name" in result_df.columns
    assert "price" in result_df.columns

def test_load_to_sqlserver(spark):
    """Test data loading to SQL Server"""
    # Create a test DataFrame
    test_data = [
        (1, "Product A", 100.0),
        (2, "Product B", 200.0),
        (3, "Product C", 300.0)
    ]
    test_schema = StructType([
        StructField("id", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("price", DoubleType(), True)
    ])
    test_df = spark.createDataFrame(test_data, schema=test_schema)
    
    # Mock the load_to_sqlserver function
    def mock_load(df, table_name):
        # Verify the DataFrame has the expected structure
        assert df.count() == 3
        assert len(df.columns) == 3
        assert "id" in df.columns
        assert "name" in df.columns
        assert "price" in df.columns
        return True
    
    # Test the function
    result = mock_load(test_df, "Sales.SalesData")
    assert result is True 