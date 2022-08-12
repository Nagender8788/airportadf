# Databricks notebook source
# MAGIC %sql
# MAGIC --drop database raw
# MAGIC create database raw comment "this is raw data"

# COMMAND ----------

# MAGIC %sql
# MAGIC create database mart comment "this is aggregated data"