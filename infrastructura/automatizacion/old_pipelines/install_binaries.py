from dagster import graph,job, op, Definitions,OpExecutionContext
from dagster_aws.s3 import S3Resource
from dagster_shell import execute_shell_command
import logging
from utils import download_files,upload_files


@op
def create_temp_folders(context: OpExecutionContext):
    lgr = logging.getLogger('console_logger')
    lgr.error("Creating folders")
    execute_shell_command('mkdir -p /opt/binaries', output_logging="STREAM", log=context.log)
    execute_shell_command('ls -al /opt', output_logging="STREAM", log=context.log)
    return None

@op
def download_data(context: OpExecutionContext,object_input):
    download_files("binaries/","/tmp/")
    # Validate which files were downloaded
    execute_shell_command('ls -al /tmp/binaries', output_logging="STREAM", log=context.log)
    return None

@op
def extract_zip(context: OpExecutionContext,object_input):
    execute_shell_command('tar -xf /tmp/binaries/knime_4.7.5.linux.gtk.x86_64.tar.gz -C /opt/binaries', output_logging="STREAM", log=context.log)
    return None


@job
def install_binaries():
  t1=create_temp_folders()
  t2=download_data(t1)
  t3=extract_zip(t2)

defs = Definitions(
    jobs=[install_binaries],
    resources={'s3': S3Resource(
                     region_name= 'us-east-1',
                     endpoint_url= 'http://myminio:9000',
                     aws_access_key_id= "test",
                     aws_secret_access_key= "r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G"

                                )}
)