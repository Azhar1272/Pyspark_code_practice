from pyspark.sql import *
from pyspark.sql import functions as f
from pyspark.sql import types as t

def pyspark_sql_lib():
    return f,t

def create_spark_session():
    spark = SparkSession.builder \
                    .appName("Hello_spark") \
                    .master("local[3]") \
                    .getOrCreate()
    return spark

def read_csv(path,header=True) -> DataFrame:
    spark = create_spark_session()
    df = spark.read.format("csv").option("header",header).load(path)
    return df

def read_json(path) -> DataFrame:
    spark = create_spark_session()
    df = spark.read.option("multiline","true")\
    .json(path)
    return df
