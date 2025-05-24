from pyspark.sql import SparkSession

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("TestSparkJob") \
        .getOrCreate()

    # Create a simple DataFrame
    data = [("Java", 4000), ("Python", 1000), ("Scala", 3000)]
    df = spark.createDataFrame(data, ["language", "users_count"])

    # Perform some operations
    df.show()
    df.write.mode("overwrite").parquet("/opt/bitnami/spark/data/output/test_output")

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main() 