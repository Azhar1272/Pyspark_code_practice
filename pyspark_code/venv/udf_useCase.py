from utils import spark_utils
from utils import spark_udf
f,t = spark_utils.pyspark_sql_lib()
from pyspark.sql.functions import *
path_csv = "data/england_councils/district_councils.csv"

def upperCase(col):
    return col.upper()

upperCaseUDF = udf(upperCase, StringType())

df = spark_utils.read_csv(path_csv)
#df.show()
df2 = df.withColumn("country", upperCaseUDF(lit("abc")))
df2.show()