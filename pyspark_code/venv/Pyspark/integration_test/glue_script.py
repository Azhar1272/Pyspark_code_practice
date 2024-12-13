from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import DataFrame

def transform_data(df: DataFrame) -> DataFrame:
    """Example transformation: add a new column."""
    return df.withColumn("new_column", df["existing_column"] * 2)

def main():
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session

    # Load the data
    source_df = spark.read.json("s3://example-bucket/input-data/")
    transformed_df = transform_data(source_df)

    # Write the data
    transformed_df.write.json("s3://example-bucket/output-data/")
