# Databricks notebook source
flightsdf= spark.sql("select  * from raw.flights")
display(flightsdf)
flightsdf.printSchema()

# COMMAND ----------

from pyspark.sql.functions import *
delaydf = flightsdf.select("AIRLINE_DELAY","WEATHER_DELAY","AIR_SYSTEM_DELAY").filter(col("AIRLINE_DELAY")>0)
display(delaydf)

# COMMAND ----------

# MAGIC %sql
# MAGIC use raw

# COMMAND ----------

#Airport with highest number of pasengers airvials
df = spark.sql("select count(*) as flightscount from flights group by(ORIGIN_AIRPORT, DESTINATION_AIRPORT) ")
df.display()
