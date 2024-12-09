from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list, row_number
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("DynamicColumns").getOrCreate()

# Input data
data = [("sh", "eml1"), ("sh", "eml2"), ("sh", "eml3"),
        ("az", "emzl1"), ("az", "emzl2")]

columns = ["user", "email"]
df = spark.createDataFrame(data, columns)

# Step 1: Add a row number for each email per user
window = Window.partitionBy("user").orderBy("email")
df_with_index = df.withColumn("email_index", row_number().over(window))
df_with_index.show()

# Step 2: Pivot the data to create dynamic email columns
pivot_df = df_with_index.groupBy("user").pivot("email_index").agg(collect_list("email"))
pivot_df.show()

# Step 3: Rename columns to email1, email2, etc.
renamed_columns = [col for col in pivot_df.columns]
print(renamed_columns)
for i, column in enumerate(renamed_columns[1:], start=1):  # Skip the first 'user' column
    print(i,column)
    renamed_columns[i] = f"email{i}"

pivot_df = pivot_df.toDF()

# Show the result
pivot_df.show()