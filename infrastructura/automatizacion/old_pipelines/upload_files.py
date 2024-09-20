from dagster import graph,job, op, Definitions,OpExecutionContext
from dagster_aws.s3 import S3Resource
from dagster_shell import execute_shell_command
import logging
from utils import download_files,upload_files


@op
def upload_data(context: OpExecutionContext):
    execute_shell_command(f"ls -al /opt/data/processed/", output_logging="STREAM", log=context.log)
    upload_files("/opt/data/processed/","processed")
    return None


@job
def upload_job():
  t3a=upload_data()

defs = Definitions(
    jobs=[upload_job],
    resources={'s3': S3Resource(
                     region_name= 'us-east-1',
                     endpoint_url= 'http://myminio:9000',
                     aws_access_key_id= "test",
                     aws_secret_access_key= "r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G"

                                )}
)