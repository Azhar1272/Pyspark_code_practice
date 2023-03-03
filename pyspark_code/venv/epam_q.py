from utils import spark_utils
f,t = spark_utils.pyspark_sql_lib()
## use of explode,collect_ws,,regexp_replace,split

path_json = "data/json/epam.json"
path_csv = "data/england_councils/district_councils.csv"

df = spark_utils.read_csv(path_csv)
df.show(truncate=False)
df = spark_utils.read_json(path_json)
df.show(truncate=False)

df_split = df.withColumn("split_text",f.split("text"," ")).select("user","split_text")
df_explode = df_split.select("user",f.explode("split_text").alias("explode_text"))
df_hash = df_explode.filter(f.col("explode_text").like('#%'))

df_collect = df_hash.groupBy("user").agg(f.collect_set(f.regexp_replace("explode_text","#","")).alias("collect_hash"))
df_final = df_collect.select("user", f.concat_ws(',',"collect_hash").alias("collected#"))

df_final.show(truncate=False)

df_hash_count = df_hash.groupBy("explode_text").agg(f.count("*").alias("count_of_hash"))\
                       .select(f.regexp_replace("explode_text","#","").alias("text"),"count_of_hash")
df_hash_count.show(truncate=False)


"""
Input
+-----+----------------+---------------------------------------------------------------------+-------+
|id   |place           |text                                                                 |user   |
+-----+----------------+---------------------------------------------------------------------+-------+
|53627|Hyderabad, INDIA|epam_rocks epam_internal #EPAM HACKATON ROCKS #Love #EPAM #Hackathons|EPAM_BD|
|53628|Hyderabad, INDIA|#epam_rocks_again                                                    |EPAM_BD|
|53629|Hyderabad, INDIA|#Hyderabad                                                           |Joe    |
+-----+----------------+---------------------------------------------------------------------+-------+

Find out all the hashtags mentioned on a tweet per user

Output
+-------+-------------------------------------+
|user   |collected#                           |
+-------+-------------------------------------+
|Joe    |Hyderabad                            |
|EPAM_BD|Hackathons,EPAM,epam_rocks_again,Love|
+-------+-------------------------------------+

Count how many times each hashtag is mentioned across all users

Output
+----------------+-------------+
|text            |count_of_hash|
+----------------+-------------+
|Love            |1            |
|Hackathons      |1            |
|EPAM            |2            |
|Hyderabad       |1            |
|epam_rocks_again|1            |
+----------------+-------------+
"""