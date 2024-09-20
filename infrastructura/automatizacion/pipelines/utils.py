import logging
import boto3
import pandas as pd
import io
from pathlib import Path
import os

def escribir_archivo(*op_args, **kwargs):
  scw = boto3.Session(region_name="us-east-1")
  source=op_args[0]
  target=op_args[1]
  print(f"Intentar escribir en {target}")
  s3 = scw.resource('s3',endpoint_url="http://myminio:9000", aws_access_key_id="test", aws_secret_access_key="r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G" )
  s3_object = s3.Object(
      bucket_name='proyecto',
      key=target
  )
  f = open(source, "r")
  s3_object.put(Body=f.read())

def obtener_archivo(relative_path,s3_path, file_name):
  scw = boto3.Session(region_name="us-east-1")
  s3 = scw.resource('s3',endpoint_url="http://myminio:9000", aws_access_key_id="test", aws_secret_access_key="r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G" )
  s3_object = s3.Object(
      bucket_name='proyecto',
      key=f"{s3_path}/{file_name}"
  )
  s3_response = s3_object.get()
  s3_object_body = s3_response.get('Body')
  content_str = s3_object_body.read().decode('latin1')
  f = open(f"{relative_path}/{file_name}", "a")
  f.write(content_str)
  f.close()


def get_file_folders(s3_client, bucket_name, prefix=""):
    file_names = []
    folders = []

    default_kwargs = {
        "Bucket": bucket_name,
        "Prefix": prefix
    }
    next_token = ""

    while next_token is not None:
        updated_kwargs = default_kwargs.copy()
        if next_token != "":
            updated_kwargs["ContinuationToken"] = next_token

        response = s3_client.list_objects_v2(**default_kwargs)
        contents = response.get("Contents")

        for result in contents:
            key = result.get("Key")
            if key[-1] == "/":
                folders.append(key)
            else:
                file_names.append(key)

        next_token = response.get("NextContinuationToken")

    return file_names, folders


def download_files( s3_prefix, local_path):
    client = boto3.client('s3',endpoint_url="http://myminio:9000", aws_access_key_id="test", aws_secret_access_key="r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G" )
    scw = boto3.Session(region_name="us-east-1")
    s3 = scw.resource('s3',endpoint_url="http://myminio:9000", aws_access_key_id="test", aws_secret_access_key="r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G" )
    download_dir(client, s3, s3_prefix, local_path, bucket='proyecto')

def download_dir(client, resource, dist, local='/tmp', bucket='your_bucket'):
    paginator = client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                download_dir(client, resource, subdir.get('Prefix'), local, bucket)
        for file in result.get('Contents', []):
            dest_pathname = os.path.join(local, file.get('Key'))
            if not os.path.exists(os.path.dirname(dest_pathname)):
                os.makedirs(os.path.dirname(dest_pathname))
            if not file.get('Key').endswith('/'):
                resource.meta.client.download_file(bucket, file.get('Key'), dest_pathname)

def upload_files(local_path, s3_path):
    client = boto3.client('s3',endpoint_url="http://myminio:9000", aws_access_key_id="test", aws_secret_access_key="r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G" )
    scw = boto3.Session(region_name="us-east-1")
    s3 = scw.resource('s3',endpoint_url="http://myminio:9000", aws_access_key_id="test", aws_secret_access_key="r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G" )
    print(local_path)
    for root,dirs,files in os.walk(local_path):
        print("==========================")
        print(files)
        logging.error(root)
        for file in files:
            logging.error(file)
            client.upload_file(os.path.join(root,file),"proyecto",f"{s3_path}/{file}")
