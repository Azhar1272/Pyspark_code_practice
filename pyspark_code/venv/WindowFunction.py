from utils import spark_utils
from pyspark.sql import *
f,t = spark_utils.pyspark_sql_lib()
spark = SparkSession.builder \
    .appName("Hello_spark") \
    .master("local[3]") \
    .getOrCreate()

data = [("James", "Sales", 3000), \
    ("Michael", "Sales", 4600),  \
    ("Robert", "Sales", 4100),   \
    ("Maria", "Finance", 3000),  \
    ("James", "Sales", 3000),    \
    ("Scott", "Finance", 3300),  \
    ("Jen", "Finance", 3900),    \
    ("Jeff", "Marketing", 3000), \
    ("Kumar", "Marketing", 2000),\
    ("Saif", "Sales", 4100) \
    ]

columns= ["name","dep","sal"]

df = spark.createDataFrame(data, columns)
df.show()

