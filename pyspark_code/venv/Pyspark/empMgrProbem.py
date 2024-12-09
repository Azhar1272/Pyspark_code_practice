from pyspark.sql.window import Window
from pyspark.sql import *
from pyspark.sql.functions import *
emp = [(1,"Smith",-1,"2018","10","M",3000), \
    (2,"Rose",1,"2010","20","M",4000), \
    (3,"Williams",1,"2010","10","M",1000), \
    (4,"Jones",2,"2005","10","F",2000), \
    (5,"Brown",2,"2010","40","",3000), \
      (6,"Brown",2,"2010","50","",1500) \
  ]
empColumns = ["emp_id","name","superior_emp_id","year_joined", \
       "Emp_dept_id","gender","salary"]

empDF = spark.createDataFrame(data=emp, schema = empColumns)

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]
deptColumns = ["dept_name","dept_id"]

deptDF = spark.createDataFrame(data=dept, schema = deptColumns)

empDF.show()

emp_dep = empDF.join(deptDF, col('Emp_dept_id') == col('dept_id'), 'inner')
win = Window.partitionBy('dept_name').orderBy(col('salary').desc())
emp_lead = emp_dep.select('name','salary','dept_name',lead('salary',2).over(win).alias('lead')).show()
emp_dep.show()


df_final = (
              empDF.alias('emp').join(empDF.alias('mgr'),
                                        col('emp.superior_emp_id') == col('mgr.emp_id'),
                                        'left'
                                      ).select(
                                          col('emp.emp_id'),
                                          col('emp.name'),
                                          coalesce(col('mgr.name'),lit('sm')).alias('managerName')
                                      )
                  )

df_final.show()

'''
+------+--------+---------------+-----------+-----------+------+------+
|emp_id|    name|superior_emp_id|year_joined|Emp_dept_id|gender|salary|
+------+--------+---------------+-----------+-----------+------+------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|
|     2|    Rose|              1|       2010|         20|     M|  4000|
|     3|Williams|              1|       2010|         10|     M|  1000|
|     4|   Jones|              2|       2005|         10|     F|  2000|
|     5|   Brown|              2|       2010|         40|      |  3000|
|     6|   Brown|              2|       2010|         50|      |  1500|
+------+--------+---------------+-----------+-----------+------+------+

+--------+------+---------+----+
|    name|salary|dept_name|lead|
+--------+------+---------+----+
|   Smith|  3000|  Finance|1000|
|   Jones|  2000|  Finance|NULL|
|Williams|  1000|  Finance|NULL|
|   Brown|  3000|       IT|NULL|
|    Rose|  4000|Marketing|NULL|
+--------+------+---------+----+

+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|    name|superior_emp_id|year_joined|Emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|  Finance|     10|
|     3|Williams|              1|       2010|         10|     M|  1000|  Finance|     10|
|     4|   Jones|              2|       2005|         10|     F|  2000|  Finance|     10|
|     2|    Rose|              1|       2010|         20|     M|  4000|Marketing|     20|
|     5|   Brown|              2|       2010|         40|      |  3000|       IT|     40|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+

+------+--------+-----------+
|emp_id|    name|managerName|
+------+--------+-----------+
|     2|    Rose|      Smith|
|     1|   Smith|         sm|
|     3|Williams|      Smith|
|     4|   Jones|       Rose|
|     5|   Brown|       Rose|
|     6|   Brown|       Rose|
+------+--------+-----------+
'''