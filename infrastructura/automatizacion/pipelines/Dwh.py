from dagster import graph,job, op, Definitions,OpExecutionContext
import logging
from utils import subir_archivo,descargar_archivo
from db_utils import ejecutar_sql
from dagster import asset, Config
from dagster import job, materialize, op, RunConfig
import json 
import os
import pandas as pd
import io   
from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month, day
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType
#from utils import download_files,upload_files
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

@op
def escribir_en_dwh_productos():
  spark = SparkSession.builder.appName("ReadFilterProducts").config("spark.jars.packages", "org.postgresql:postgresql:42.6.0").getOrCreate()
  path="parquet_transformado/productos"
  categoria_id='*'
  marca_id=1
  final_path = path
  if categoria_id is not None:
      final_path = f"{path}/categoria_id={categoria_id}"
  if marca_id is not None:
       final_path = f"{final_path}/marca_id={marca_id}"
  data = spark.read.option("header", True)\
      .option("inferSchema", "true") \
      .option("basePath", path) \
      .csv(final_path)
  
  print(data.show())
  postgres_properties = {
      "user": os.getenv("DB_USER"),
      "password": os.getenv("DB_PASSWORD"),"driver" : "org.postgresql.Driver"  }

  postgres_url = f"jdbc:postgresql://{os.getenv("DB_HOST", "localhost")}:5432/dwh"
  print(postgres_url)
  try:
    pass
   
    # Write dimension tables
    data.write.format("jdbc") \
      .option("mode", "overwrite") \
      .option("url", postgres_url) \
      .option("dbtable", "producto") \
      .options(**postgres_properties).save()
  except Exception as e:
      print(f"Error writing to data warehouse: {str(e)}")
      raise

@op
def escribir_en_dwh_evento():
  spark = SparkSession.builder.appName("ReadFilterEventos").config("spark.jars.packages", "org.postgresql:postgresql:42.6.0").getOrCreate()
  path="parquet_transformado/eventos"
  evento_nombre='*'
  if evento_nombre is not None:
      final_path = f"{path}/event={evento_nombre}"
  data = spark.read.option("header", True)\
      .option("inferSchema", "true") \
      .option("basePath", path) \
      .csv(final_path)
  
  postgres_properties = {
      "user": os.getenv("DB_USER"),
      "password": os.getenv("DB_PASSWORD"),"driver" : "org.postgresql.Driver"  }

  postgres_url = f"jdbc:postgresql://{os.getenv("DB_HOST", "localhost")}:5432/dwh"
  print(postgres_url)
  try:
    pass
    # Write dimension tables
    data.write.format("jdbc") \
      .option("mode", "overwrite") \
      .option("url", postgres_url) \
      .option("dbtable", "eventos") \
      .options(**postgres_properties).save()
  except Exception as e:
      print(f"Error writing to data warehouse: {str(e)}")
      raise


@op
def escribir_en_dwh_clientes():
  spark = SparkSession.builder.appName("ReadFilterClients").config("spark.jars.packages", "org.postgresql:postgresql:42.6.0").getOrCreate()
  path="parquet_transformado/clientes"
  genero_nombre='*'
  if genero_nombre is not None:
      final_path = f"{path}/genero={genero_nombre}"
  data = spark.read.option("header", True)\
      .option("inferSchema", "true") \
      .option("basePath", path) \
      .csv(final_path)
  
  postgres_properties = {
      "user": os.getenv("DB_USER"),
      "password": os.getenv("DB_PASSWORD"),"driver" : "org.postgresql.Driver"  }

  postgres_url = f"jdbc:postgresql://{os.getenv("DB_HOST", "localhost")}:5432/dwh"
  print(postgres_url)
  try:
    pass
    # Write dimension tables
    data.write.format("jdbc") \
      .option("mode", "overwrite") \
      .option("url", postgres_url) \
      .option("dbtable", "clientes") \
      .options(**postgres_properties).save()
  except Exception as e:
      print(f"Error writing to data warehouse: {str(e)}")
      raise
    
@job
def carga_dwh_productos():
  t0 = escribir_en_dwh_productos()

@job
def carga_dwh_eventos():
  t0 = escribir_en_dwh_evento()

@job
def carga_dwh_clientes():
  t0 = escribir_en_dwh_clientes()

defs = Definitions(
    jobs=[carga_dwh_productos,carga_dwh_eventos,carga_dwh_clientes],
    assets=[],
    resources={}
)