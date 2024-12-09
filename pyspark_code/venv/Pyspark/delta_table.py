from delta.tables import *

data = [("Alice", 29), ("Bob", 35), ("Charlie", 23)]
columns = ["name", "age"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Write DataFrame as a Delta Lake table
df.write.format("delta").save("s3://your-bucket/delta-table")