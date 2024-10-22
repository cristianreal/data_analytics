import logging
import boto3
import pandas as pd
import io
from pathlib import Path
import os

_aws_access_key_id="test123456"
_aws_secret_access_key="test123456"
_endpoint_url="http://myminio:9000"
_bucket_name='datalake'

def subir_archivo(local_path, s3_path):
    client = boto3.client('s3',endpoint_url=_endpoint_url, aws_access_key_id=_aws_access_key_id, aws_secret_access_key=_aws_secret_access_key )
    scw = boto3.Session(region_name="us-east-1")
    s3 = scw.resource('s3',endpoint_url=_endpoint_url, aws_access_key_id=_aws_access_key_id, aws_secret_access_key=_aws_secret_access_key )
    print(local_path)
    for root,dirs,files in os.walk(local_path):
        logging.debug(root)
        for file in files:
            logging.debug(file)
            local_file_path = os.path.join(root, file)
            # Calculate the relative path
            relative_path = os.path.relpath(local_file_path, local_path)
            # Construct the S3 key (path in the bucket)
            s3_key = os.path.join(s3_path, relative_path).replace("\\", "/")
            client.upload_file(local_file_path,_bucket_name,s3_key)
            
def descargar_archivo(relative_path,s3_path, file_name):
  content_str = obtener_datos(s3_path, file_name)
  f = open(f"{relative_path}/{file_name}", "w")
  f.write(content_str)
  f.close()


def obtener_datos(s3_path, file_name):
  scw = boto3.Session(region_name="us-east-1")
  s3 = scw.resource('s3',endpoint_url=_endpoint_url, aws_access_key_id=_aws_access_key_id, aws_secret_access_key=_aws_secret_access_key )
  s3_object = s3.Object(
      bucket_name=_bucket_name,
      key=f"{s3_path}/{file_name}"
  )
  s3_response = s3_object.get()
  s3_object_body = s3_response.get('Body')
  content_str = s3_object_body.read().decode('latin1')
  return content_str

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
    client = boto3.client('s3',endpoint_url=_endpoint_url, aws_access_key_id=_aws_access_key_id, aws_secret_access_key=_aws_secret_access_key )
    scw = boto3.Session(region_name="us-east-1")
    s3 = scw.resource('s3',endpoint_url=_endpoint_url, aws_access_key_id=_aws_access_key_id, aws_secret_access_key=_aws_secret_access_key )
    download_dir(client, s3, s3_prefix, local_path, bucket=_bucket_name)

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

