from dagster import graph,job, op, Definitions,OpExecutionContext
from dagster_aws.s3 import S3Resource
from dagster_shell import execute_shell_command
import logging
from utils import download_files,upload_files

@op
def create_temp_folders(context: OpExecutionContext):
    lgr = logging.getLogger('console_logger')
    lgr.error("Creating folders")
    execute_shell_command('mkdir -p /opt/data/db', output_logging="STREAM", log=context.log)
    execute_shell_command('ls -al /opt/data', output_logging="STREAM", log=context.log)
    return None

@op
def download_data(context: OpExecutionContext,object_input):
    download_files("db/","/opt/data/")
    # Validate which files were downloaded
    execute_shell_command('ls -al /opt/data', output_logging="STREAM", log=context.log)
    execute_shell_command('ls -al /opt/data/db', output_logging="STREAM", log=context.log)
    return None

@op
def execute_knime_workflow_load(context: OpExecutionContext,object_input):
    knime_path='/opt/binaries/knime_4.7.5/knime'
    knime_workflow='/opt/knime_scripts/2. Load_Data.knwf'
    input_data='/opt/data/db'
    db_username='proyectointegrador'
    db_password='proyectointegrador'
    db_name='proyectointegrador'
    db_server='postgres'
    # Validate which files were downloaded
    execute_shell_command(f"{knime_path} --launcher.suppressErrors -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION  -workflowFile=\"{knime_workflow}\" \
        -workflow.variable=input_folder,{input_data},String \
        -workflow.variable=db_username,\"{db_username}\",String \
        -workflow.variable=db_password,\"{db_password}\",String \
        -workflow.variable=db_name,\"{db_name}\",String \
        -workflow.variable=db_server,\"{db_server}\",String", output_logging="STREAM", log=context.log)
    return None

@job
def load_to_database_job():
  t0=create_temp_folders()
  t1=download_data(t0)
  t3=execute_knime_workflow_load(t1)

defs = Definitions(
    jobs=[load_to_database_job],
    resources={'s3': S3Resource(
                     region_name= 'us-east-1',
                     endpoint_url= 'http://myminio:9000',
                     aws_access_key_id= "test",
                     aws_secret_access_key= "r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G"

                                )}
)