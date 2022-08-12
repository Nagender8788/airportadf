# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",

           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",

           "fs.azure.account.oauth2.client.id": "28230ad6-a470-4704-a9bd-acd6ed334730",

           "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="myscope",key="AppRegiSecreatinKeyValut"),

           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/e17b8925-d51a-47d4-a33f-c4a1110de4b4/oauth2/token"}

# COMMAND ----------

# normal cvs files monting
dbutils.fs.mount(

  source = "abfss://sinkstorage@airportadlsgen2.dfs.core.windows.net/",

  mount_point = "/mnt/airportadata",

  extra_configs = configs)

# COMMAND ----------

# zip files monting
dbutils.fs.mount(

  source = "abfss://zipsource@airportadlsgen2.dfs.core.windows.net/",

  mount_point = "/mnt/airportzipdata",

  extra_configs = configs)

# COMMAND ----------

# MAGIC %fs ls /mnt/airportzipdata/flights

# COMMAND ----------

# MAGIC %fs ls /mnt/airportadata

# COMMAND ----------

# MAGIC %sh
# MAGIC unzip dbfs:/mnt/airportadata/flights