from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SalesETL_cicd").getOrCreate()

data = [("A",100),("B",200)]
columns=["product","sales"]

df=spark.createDataFrame(data,columns)

df.show()