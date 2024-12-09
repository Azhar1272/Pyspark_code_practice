# Read Parquet
parquet_df = spark.read.format("parquet") \
    .option("mergeSchema", "true") \
    .option("recursiveFileLookup", "true") \
    .load("s3://your-bucket/parquet-data/")

# Read CSV
csv_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .load("s3://your-bucket/csv-data/")



# Write as Parquet with partitioning and compression
df.write.format("parquet") \
    .partitionBy("year", "month") \
    .option("compression", "snappy") \
    .mode("overwrite") \
    .save("s3://your-bucket/parquet-partitioned/")

# Write as CSV with header and custom delimiter
df.write.format("csv") \
    .option("header", "true") \
    .option("delimiter", "|") \
    .option("compression", "gzip") \
    .mode("overwrite") \
    .save("s3://your-bucket/csv-output/")
