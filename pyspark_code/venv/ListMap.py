from pyspark.sql import *
from pyspark.sql import functions as f
from pyspark.sql.window import Window
from pyspark.sql.types import StructField, StructType, StringType, MapType

spark = SparkSession.builder \
                    .master("local[3]") \
                    .appName("my_project") \
                    .getOrCreate()


data = [
    ('Azhar', [{"item": "momo", "count": 5}, {"item": "choco", "count": 10}, {"item": "pops", "count": 7}])
]

# Create DataFrame
schema = ["name", "my_map"]
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show(truncate=False)

df_explode = df.withColumn('explode_items',f.explode('my_map')).select('name','explode_items')
df_explode.show(truncate=False)
# Access values using getItem() function
df_with_values = df_explode.select(f.col("name"), \
                                   f.col("explode_items").getItem("item").alias("item"), \
                                   f.col('explode_items').getItem('count').alias('count'))
df_with_values.show()

'''
+-----+--------------------------------------------------------------------------------------+
|name |my_map                                                                                |
+-----+--------------------------------------------------------------------------------------+
|Azhar|[{count -> 5, item -> momo}, {count -> 10, item -> choco}, {count -> 7, item -> pops}]|
+-----+--------------------------------------------------------------------------------------+

+-----+----------------------------+
|name |explode_items               |
+-----+----------------------------+
|Azhar|{count -> 5, item -> momo}  |
|Azhar|{count -> 10, item -> choco}|
|Azhar|{count -> 7, item -> pops}  |
+-----+----------------------------+

+-----+-----+-----+
| name| item|count|
+-----+-----+-----+
|Azhar| momo|    5|
|Azhar|choco|   10|
|Azhar| pops|    7|
+-----+-----+-----+



'''