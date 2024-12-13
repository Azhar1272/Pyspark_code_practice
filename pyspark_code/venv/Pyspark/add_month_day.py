from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Initialize Spark session
spark = SparkSession.builder.appName("test").getOrCreate()

# Sample data
data = [
    ("2023-12-07", "event1"),
    ("2023-12-08", "event2"),
    ("2023-12-09", "event3"),
    ("2023-12-10", "event4"),
    ("2023-12-11", "event5"),
    ("2023-12-12", "event6"),
]
columns = ["event_date", "event_name"]

# Create DataFrame
df = spark.createDataFrame(data, schema=columns)

# Convert event_date to DateType if not already
df = df.withColumn("event_date", col("event_date").cast("date"))

# Get the date 5 days ago
five_days_ago = date_sub(current_date(), 5)
# Get the date 5 month ago
five_month_ago = add_months(current_date(), -5)
# Get the date 5 year ago
five_year_ago = add_months(current_date(), -60)

# Filter rows from the last 5 days
filtered_df = df.filter(col("event_date") >= five_days_ago)

# Show the result
filtered_df.show()

SELECT *
FROM your_table
WHERE event_date >= DATEADD(YEAR, -5, GETDATE());
-- DATEADD(MONTH/DAY/WEEK/HH/MM/SS, -5, GETDATE())

