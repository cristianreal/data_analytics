from dagster import graph,job, op, Definitions,OpExecutionContext
import logging
from utils import download_files,upload_files
from db_utils import ejecutar_sql
from dagster import asset, Config
from dagster import job, materialize, op, RunConfig
import json 
import os

class ComandoSQL(Config):
    select_query: str
    select_params: list

@asset
def obtener_registros_db(ComandoSQL):
  print(ComandoSQL.select_query)
  select_results = ejecutar_sql(ComandoSQL.select_query, ComandoSQL.select_params)
  print(select_results)
  return select_results

@op
def obtener_categorias(context: OpExecutionContext):
  return obtener_registros_db(ComandoSQL(select_query="SELECT * FROM categoria", select_params=[]))


@op
def obtener_clientes(context: OpExecutionContext):
  return obtener_registros_db(ComandoSQL(select_query="SELECT * FROM cliente", select_params=[]))

@op
def obtener_eventos(context: OpExecutionContext,object_input):
  return obtener_registros_db(ComandoSQL(select_query="SELECT * FROM events", select_params=[]))


@op
def obtener_marcas(context: OpExecutionContext,object_input):
  return obtener_registros_db(ComandoSQL(select_query="SELECT * FROM marca", select_params=[]))


@op
def obtener_productos(context: OpExecutionContext,object_input):
  return obtener_registros_db(ComandoSQL(select_query="SELECT * FROM producto", select_params=[]))

@op
def guardar_en_datalake(object_input):
  print("guardar")
  print(object_input)
  return None


@job
def extraccion_carga_categorias():
  t0 = obtener_categorias()
  guardar_en_datalake(t0)

@job
def extraccion_carga_clientes():
  t0 = obtener_clientes()
  guardar_en_datalake(t0)

@job
def extraccion_carga_eventos():
  t0 = obtener_eventos()
  guardar_en_datalake(t0)


@job
def extraccion_carga_marca():
  t0 = obtener_marcas()
  guardar_en_datalake(t0)


@job
def extraccion_carga_producto():
  t0 = obtener_productos()
  guardar_en_datalake(t0)

defs = Definitions(
    jobs=[extraccion_carga_categorias,extraccion_carga_clientes,extraccion_carga_eventos,extraccion_carga_marca,extraccion_carga_producto],
    assets=[],
    resources={}
)