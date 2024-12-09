from pyspark.sql import *
from pyspark.sql.functions import  *
from pyspark.sql.window import Window

spark = SparkSession.builder.\
        master("local[2]").\
        appName("dev").\
        getOrCreate()

data = [("u1", "login", "2024-01-01 10:00:00"), \
    ("u2", "login", "2024-01-01 11:00:00"),  \
    ("u2", "purchase", "2024-01-01 11:00:50"),   \
    ("u1", "logout", "2024-02-01 10:00:40"),  \
    ("u3", "login", "2024-01-01 12:00:00"),    \
    ("u1", "login", "2024-01-01 10:01:00"),  \
    ("u2", "logout", "2024-01-01 11:01:00"),    \
    ("u3", "purchase", "2024-01-01 12:01:00"), \
    ("u3", "logout", "2024-01-01 12:02:00"),\
    ("u1", "purchase", "2024-01-01 10:02:00") \
    ]

columns= ["user","event_type","time_stamp"]

df = spark.createDataFrame(data,columns)

#df.show()

win = Window.partitionBy('user').orderBy('time_stamp')

## use of unix_timestamp for seconds
##Minutes: Divide seconds_diff by 60.
##Hours: Divide seconds_diff by 3600.
##Days: Divide seconds_diff by 86400.

df_final_1 = (df.withColumn('next_time_stamp',lead('time_stamp').over(win))
                .withColumn('time_duration',unix_timestamp(col('next_time_stamp')) - unix_timestamp(col('time_stamp')))
)
df_final_1.show()
df_final = df_final_1.groupBy('user').agg(avg(col('time_duration')).alias('user avg time'))
df_final.show()

'''

+----+----------+-------------------+-------------------+-------------+
|user|event_type|         time_stamp|    next_time_stamp|time_duration|
+----+----------+-------------------+-------------------+-------------+
|  u1|     login|2024-01-01 10:00:00|2024-01-01 10:01:00|           60|
|  u1|     login|2024-01-01 10:01:00|2024-01-01 10:02:00|           60|
|  u1|  purchase|2024-01-01 10:02:00|2024-02-01 10:00:40|      2678320|
|  u1|    logout|2024-02-01 10:00:40|               NULL|         NULL|
|  u2|     login|2024-01-01 11:00:00|2024-01-01 11:00:50|           50|
|  u2|  purchase|2024-01-01 11:00:50|2024-01-01 11:01:00|           10|
|  u2|    logout|2024-01-01 11:01:00|               NULL|         NULL|
|  u3|     login|2024-01-01 12:00:00|2024-01-01 12:01:00|           60|
|  u3|  purchase|2024-01-01 12:01:00|2024-01-01 12:02:00|           60|
|  u3|    logout|2024-01-01 12:02:00|               NULL|         NULL|
+----+----------+-------------------+-------------------+-------------+

+----+-----------------+
|user|    user avg time|
+----+-----------------+
|  u1|892813.3333333334|
|  u2|             30.0|
|  u3|             60.0|
+----+-----------------+

'''