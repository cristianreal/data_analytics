from dagster import graph,job, op, Definitions,OpExecutionContext
from dagster_aws.s3 import S3Resource
from dagster_shell import execute_shell_command
import logging
from utils import download_files,upload_files

@op
def download_data(context: OpExecutionContext):
    download_files("knime_scripts/","/opt/")
    # Validate which files were downloaded
    execute_shell_command('ls -al /opt/knime_scripts', output_logging="STREAM", log=context.log)
    return None

@job
def example_job():
  t1=download_data()

defs = Definitions(
    jobs=[example_job],
    resources={'s3': S3Resource(
                     region_name= 'us-east-1',
                     endpoint_url= 'http://myminio:9000',
                     aws_access_key_id= "test",
                     aws_secret_access_key= "r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G"

                                )}
)