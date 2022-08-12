# Databricks notebook source
# MAGIC %sql
# MAGIC use raw

# COMMAND ----------

airlinesdf = spark.read.format("csv").load("dbfs:/mnt/airportadata/airlines.csv",header="true",inferSchema="true")

# COMMAND ----------

airlinesdf.write.saveAsTable("airlines")

# COMMAND ----------

display(airlinesdf.distinct())

# COMMAND ----------

airportsdf = spark.read.format("csv").load("dbfs:/mnt/airportadata/airports.csv",header="true",inferSchema="true")

# COMMAND ----------

airportsdf.write.saveAsTable("airport")

# COMMAND ----------

display(airportsdf.distinct())

# COMMAND ----------

flightsdf = spark.read.format("csv").load("dbfs:/mnt/airportzipdata/flights",header="true",inferSchema="true")
flightsdfnullremoved = flightsdf.fillna(0).fillna('')
display(flightsdfnullremoved)

# COMMAND ----------

flightsdfnullremoved.write.saveAsTable("flights")

# COMMAND ----------

flightsdfuniquerecords = flightsdf.dropna(how="all");
flightsdfuniquerecords.count()

# COMMAND ----------

flightsdf.count()