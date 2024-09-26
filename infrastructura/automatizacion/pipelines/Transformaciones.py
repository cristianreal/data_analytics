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

class ArchivoS3(Config):
    nombre_archivo: str
    ruta_s3: str

@asset
def obtener_archivo_crudo(ArchivoS3):
  print(f"{ArchivoS3.ruta_s3}/{ArchivoS3.nombre_archivo}")
  ruta_relativa = "parquet_temporal/"
  os.makedirs(ruta_relativa, exist_ok=True)
  descargar_archivo(ruta_relativa, ArchivoS3.ruta_s3, ArchivoS3.nombre_archivo)
  data = pd.read_csv(f"{ruta_relativa}/{ArchivoS3.nombre_archivo}", sep=",") 
  print(data.head())
  return data

@asset
def procesar_categorias(context: OpExecutionContext):
  data = obtener_archivo_crudo(ArchivoS3(nombre_archivo="categoria.csv",ruta_s3="datos_crudos"))
  # Ejecutar transformaciones
  return data, "categorias"

@asset
def procesar_clientes(context: OpExecutionContext):
  data = obtener_archivo_crudo(ArchivoS3(nombre_archivo="cliente.csv",ruta_s3="datos_crudos"))
  # Ejecutar transformaciones
  return data,"clientes"

@asset
def procesar_eventos(context: OpExecutionContext):
  data = obtener_archivo_crudo(ArchivoS3(nombre_archivo="events.csv",ruta_s3="datos_crudos"))
  # Ejecutar transformaciones
  return data,"eventos"

@asset
def procesar_marcas(context: OpExecutionContext):
  data = obtener_archivo_crudo(ArchivoS3(nombre_archivo="marca.csv",ruta_s3="datos_crudos"))
  # Ejecutar transformaciones
  return data,"marcas"


@asset
def procesar_productos(context: OpExecutionContext):
  data = obtener_archivo_crudo(ArchivoS3(nombre_archivo="producto.csv",ruta_s3="datos_crudos"))
  # Ejecutar transformaciones
  return data,"productos"

@op
def guardar_en_datalake(df_categorias,df_marca,df_producto):
  print("guardar en data lake")
  tmp_df_marca=df_marca[0].rename(columns={"id": "marca_id"})
  tmp_df_categorias=df_categorias[0].rename(columns={"id": "categoria_id"})
  df_productos_transformado = pd.merge(df_producto[0],tmp_df_marca)
  df_productos_transformado = pd.merge(df_productos_transformado,tmp_df_categorias)
  df_productos_transformado=df_productos_transformado.rename(columns={"id": "itemid"})
  print(df_productos_transformado.columns)
  os.makedirs(f"parquet_transformado/productos", exist_ok=True)
  spark = SparkSession.builder.appName("ProductPartitioning").getOrCreate()
  spark_df = spark.createDataFrame(df_productos_transformado)
  spark_df = spark_df.withColumn("categoria_id", col("categoria_id").cast(IntegerType()))
  spark_df = spark_df.withColumn("marca_id", col("marca_id").cast(IntegerType()))
  spark_df.write \
    .partitionBy("categoria_id", "marca_id") \
    .format("parquet") \
    .mode("overwrite") \
    .save("parquet_transformado/productos")
  spark.stop()
  # resultados = object_input[0]
  # nombre_archivo = object_input[1]
  # df = pd.DataFrame(resultados)
  # 
  # df.to_parquet(f"parquet/{nombre_archivo}/{nombre_archivo}.parquet.gzip", compression='gzip')  
  subir_archivo(f"parquet_transformado/productos",f"datos_procesados")
  return None


@job
def transformacion_productos():
  df_categorias = procesar_categorias()
  df_marca = procesar_marcas()
  df_producto = procesar_productos()
  guardar_en_datalake(df_categorias,df_marca,df_producto)

@job
def transformacion_clientes():
  t0 = procesar_clientes()
  guardar_en_datalake(t0)

@job
def transformacion_eventos():
  t0 = procesar_eventos()
  guardar_en_datalake(t0)


defs = Definitions(
    jobs=[transformacion_productos,transformacion_clientes,transformacion_eventos],
    assets=[procesar_categorias,procesar_clientes, procesar_eventos, procesar_productos, procesar_marcas],
    resources={}
)