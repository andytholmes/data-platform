from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType, BooleanType

def create_spark_session():
    return SparkSession.builder \
        .appName("ETL Job") \
        .getOrCreate()

def process_data(spark, input_path, output_path):
    # Define the schema for the JSON data
    schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("price", DoubleType(), True),
        StructField("category", StringType(), True),
        StructField("in_stock", BooleanType(), True)
    ])
    
    # Read input JSON with schema
    df = spark.read.schema(schema).json(input_path)
    
    # Drop rows with NULL values in any column
    df_cleaned = df.dropna()
    
    # Write output as newline-delimited JSON
    df_cleaned.write \
        .mode("overwrite") \
        .json(output_path)

def main():
    spark = create_spark_session()
    
    input_path = "/opt/bitnami/spark/data/input/input.json"
    output_path = "/opt/bitnami/spark/data/output"
    
    process_data(spark, input_path, output_path)
    
    spark.stop()

if __name__ == "__main__":
    main() 