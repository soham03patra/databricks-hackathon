# Databricks notebook source
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2
# MAGIC # Enables autoreload; learn more at https://docs.databricks.com/en/files/workspace-modules.html#autoreload-for-python-modules
# MAGIC # To disable autoreload; run %autoreload 0

# COMMAND ----------

print(spark)

# COMMAND ----------

# MAGIC %md
# MAGIC # start here

# COMMAND ----------

# MAGIC %pip install openai

# COMMAND ----------

import sys
sys.path.append("/Workspace/project")

# COMMAND ----------

df = spark.table("workspace.default.virtue_foundation_ghana_v_0_3_sheet_1")
display(df)

# COMMAND ----------

from pyspark.sql.functions import col

df = df.dropDuplicates()
df = df.fillna("Unknown")

display(df)

# COMMAND ----------

df = df.select(
    "name",
    "description",
    "procedure",
    "equipment",
    "capability",
    "specialties",
    "address_stateOrRegion"
)

display(df)

# COMMAND ----------

from pyspark.sql.functions import split, size

df = df.withColumn("procedure_list", split(col("procedure"), ","))
df = df.withColumn("equipment_list", split(col("equipment"), ","))
df = df.withColumn("capability_list", split(col("capability"), ","))

df = df.withColumn("num_procedures", size(col("procedure_list")))
df = df.withColumn("num_equipment", size(col("equipment_list")))

display(df)

# COMMAND ----------

df.createOrReplaceTempView("facilities")

# COMMAND ----------

df_anomaly = df.filter(
    (col("num_procedures") > 20) & (col("num_equipment") < 3)
)

display(df_anomaly)

# COMMAND ----------

df_region = df.groupBy("address_stateOrRegion").count().orderBy("count")

display(df_region)

# COMMAND ----------

from main_agent import agent

# COMMAND ----------

result = agent("how many hospitals", spark, df)
display(result)

# COMMAND ----------

result = agent("region analysis", spark, df)
display(result)

# COMMAND ----------

result = agent("anomaly detection", spark, df)
display(result)

# COMMAND ----------

import openai

openai.api_key = "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"

# COMMAND ----------


from llm_extractor import extract_organizations

text = df.select("description").first()[0]

result = extract_organizations(text)

print(result)

# COMMAND ----------

