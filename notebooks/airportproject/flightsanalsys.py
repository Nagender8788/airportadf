# Databricks notebook source
flightsdf= spark.sql("select  * from raw.flights")
display(flightsdf)
flightsdf.printSchema()

# COMMAND ----------

from pyspark.sql.functions import *
delaydf = flightsdf.select("AIRLINE_DELAY","WEATHER_DELAY","AIR_SYSTEM_DELAY").filter(col("AIRLINE_DELAY")>0)
display(delaydf)

# COMMAND ----------

