from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.master("local[1]").appName("test").getOrCreate()
spark.conf.set("spark.sql.driver.memory", "2g")

data = [("hello world are you there",)]  # Notice the comma after the string to make it a tuple
column = ["word"]
df = spark.createDataFrame(data, column)
wordcount = (
    df.withColumn("word", explode(split(col('word'), ' ')))
)
wordcount.count()