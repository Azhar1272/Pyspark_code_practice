from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *

class CouncilsJob:

    def __init__(self):
        self.spark_session = (SparkSession.builder
                              .master("local[*]")
                              .appName("EnglandCouncilsJob")
                              .getOrCreate())
        print("init")
        #self.input_directory = "data"
    def extract_councils(self):
        df1 = self.spark_session.read.format("csv").option("header", "true").load(
            "data/england_councils/district_councils.csv")
        df1 = df1.withColumn("council_type", lit("District Council"))

        df2 = self.spark_session.read.format("csv").option("header", "true").load(
            "data/england_councils/london_boroughs.csv")
        df2 = df2.withColumn("council_type", lit("London Borough"))

        df3 = self.spark_session.read.format("csv").option("header", "true").load(
            "data/england_councils/metropolitan_districts.csv")
        df3 = df3.withColumn("council_type", lit("Metropolitan District"))

        df4 = self.spark_session.read.format("csv").option("header", "true").load(
            "data/england_councils/unitary_authorities.csv")
        df4 = df4.withColumn("council_type", lit("Unitary Authority"))

        df = df1.union(df2).union(df3).union(df4)
        print("first")
        return df

    def extract_avg_price(self):
        df1 = self.spark_session.read.format("csv").option("header", "true").load("data/property_avg_price.csv")
        df2 = df1.withColumn("council", df1.local_authority).select("council", "avg_price_nov_2019")
        print("second")
        return df2

    def extract_sales_volume(self):
        df1 = self.spark_session.read.format("csv").option("header", "true").load("data/property_sales_volume.csv")
        df1 = df1.withColumn("council", df1.local_authority).select("council", "sales_volume_sep_2019")
        print("third")
        return df1

    def transform(self, councils_df, avg_price_df, sales_volume_df):
        df1 = councils_df.join(avg_price_df, councils_df.council == avg_price_df.council, "left").join(sales_volume_df,councils_df.council == sales_volume_df.council,"left").select(councils_df.council, councils_df.county, councils_df.council_type, avg_price_df.avg_price_nov_2019,sales_volume_df.sales_volume_sep_2019)
        return df1

    def run(self):
        return self.transform(self.extract_councils(),self.extract_avg_price(),self.extract_sales_volume())

a = CouncilsJob().run()
a.show()