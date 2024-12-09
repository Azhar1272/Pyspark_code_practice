from pyspark.sql import *
from pyspark.sql.functions import  *
from pyspark.sql.window import Window

spark = SparkSession.builder.\
        master("local[2]").\
        appName("dev").\
        getOrCreate()

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

df = spark.createDataFrame(data,columns)
print(df.rdd.getNumPartitions())
df.show()

df.show(truncate=False)

win = Window.partitionBy("dep").orderBy(col("sal").desc())
win1 = (Window.partitionBy("dep")
            .orderBy(col("sal").desc())
            .rowsBetween(Window.unboundedPreceding, Window.currentRow))
win2 = (Window.partitionBy("dep")
            .orderBy(col("sal").desc())
            .rowsBetween(Window.unboundedPreceding, 1))
win3 = (Window.partitionBy("dep")
            .orderBy(col("sal").desc())
            .rowsBetween(Window.unboundedPreceding, -1))

#df.select('name','dep','sal',rank().over(win).alias('rnk')).filter(col('rnk')==1).show()
df.withColumn("rb",sum('sal').over(win1)).withColumn("rb1",sum('sal').over(win2)).withColumn("rb2",sum('sal').over(win3)).show()