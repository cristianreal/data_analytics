from dagster import graph,job, op, Definitions,OpExecutionContext
from dagster_aws.s3 import S3Resource
from dagster_shell import execute_shell_command
import logging
from utils import download_files,upload_files

@op
def create_temp_folders(context: OpExecutionContext):
    lgr = logging.getLogger('console_logger')
    lgr.error("Creating folders")
    execute_shell_command('mkdir -p /opt/data/raw && mkdir -p /opt/data/sql && mkdir -p /opt/data/db && mkdir -p /opt/data/processed', output_logging="STREAM", log=context.log)
    execute_shell_command('rm -rf /opt/data/raw/*', output_logging="STREAM", log=context.log)
    execute_shell_command('rm -rf /opt/data/sql/*', output_logging="STREAM", log=context.log)
    execute_shell_command('rm -rf /opt/data/db/*', output_logging="STREAM", log=context.log)
    execute_shell_command('rm -rf /opt/data/processed/*', output_logging="STREAM", log=context.log)
    execute_shell_command('ls -al /opt/data', output_logging="STREAM", log=context.log)
    return None

@op
def download_data(context: OpExecutionContext,object_input):
    download_files("raw/","/opt/data/")
    # Validate which files were downloaded
    execute_shell_command('ls -al /opt/data', output_logging="STREAM", log=context.log)
    execute_shell_command('ls -al /opt/data/raw', output_logging="STREAM", log=context.log)
    execute_shell_command('ls -al /opt/data/raw/facturas', output_logging="STREAM", log=context.log)
    return None

@op
def download_data_db(context: OpExecutionContext,object_input):
    download_files("db/","/opt/data/")
    # Validate which files were downloaded
    execute_shell_command('ls -al /opt/data', output_logging="STREAM", log=context.log)
    execute_shell_command('ls -al /opt/data/db', output_logging="STREAM", log=context.log)
    return None

@op
def upload_data(context: OpExecutionContext,object_input):
    execute_shell_command(f"ls -al /opt/data/processed/", output_logging="STREAM", log=context.log)
    upload_files("/opt/data/processed/","processed")
    return None

@op
def execute_knime_workflow_clean(context: OpExecutionContext,object_input1):
    knime_path='/opt/binaries/knime_4.7.5/knime'
    knime_workflow='/opt/knime_scripts/1. CleanProcess.knwf'
    input_data='/opt/data/raw'
    outuput_data='/opt/data/processed'
    # Validate which files were downloaded
    execute_shell_command(f"{knime_path} --launcher.suppressErrors -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION  -workflowFile=\"{knime_workflow}\" -workflow.variable=input_folder,{input_data},String -workflow.variable=output_folder,{outuput_data},String", output_logging="STREAM", log=context.log)
    execute_shell_command(f"ls -al {outuput_data}", output_logging="STREAM", log=context.log)
    return None




@op
def execute_knime_workflow_load_csv_extra(context: OpExecutionContext,object_input):
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

@op
def execute_knime_workflow_load(context: OpExecutionContext,object_input):
    knime_path='/opt/binaries/knime_4.7.5/knime'
    knime_workflow='/opt/knime_scripts/2. Load_Data.knwf'
    input_data='/opt/data/processed'
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

@op
def execute_knime_workflow_association(context: OpExecutionContext,object_input):
    knime_path='/opt/binaries/knime_4.7.5/knime'
    knime_workflow='/opt/knime_scripts/5. Association Rules.knwf'
    db_username='proyectointegrador'
    db_password='proyectointegrador'
    db_name='proyectointegrador'
    db_server='postgres'
    # Validate which files were downloaded
    execute_shell_command(f"{knime_path} --launcher.suppressErrors -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION  -workflowFile=\"{knime_workflow}\" \
                        -workflow.variable=db_username,\"{db_username}\",String \
                        -workflow.variable=db_password,\"{db_password}\",String \
                        -workflow.variable=db_name,\"{db_name}\",String \
                        -workflow.variable=db_server,\"{db_server}\",String", output_logging="STREAM", log=context.log)
    return None

@op
def execute_knime_workflow_extra_sql(context: OpExecutionContext,object_input1,object_input2,object_input3):
    knime_path='/opt/binaries/knime_4.7.5/knime'
    knime_workflow='/opt/knime_scripts/6. Run_SQL.knwf'
    db_username='proyectointegrador'
    db_password='proyectointegrador'
    db_name='proyectointegrador'
    db_server='postgres'
    # Validate which files were downloaded
    execute_shell_command(f"{knime_path} --launcher.suppressErrors -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION  -workflowFile=\"{knime_workflow}\" \
                        -workflow.variable=db_username,\"{db_username}\",String \
                        -workflow.variable=db_password,\"{db_password}\",String \
                        -workflow.variable=db_name,\"{db_name}\",String \
                        -workflow.variable=db_server,\"{db_server}\",String", output_logging="STREAM", log=context.log)
    return None

@job
def example_job():
  t0=create_temp_folders()
  t1a=download_data(t0)
  t1b=download_data_db(t0)
  t2a=execute_knime_workflow_clean(t1a)
  t3a=upload_data(t2a)
  t3b=execute_knime_workflow_load(t2a)
  t3c=execute_knime_workflow_load_csv_extra(t1b)
  t3d=execute_knime_workflow_association(t2a)
  t4 = execute_knime_workflow_extra_sql(t3b,t3c,t3d)

defs = Definitions(
    jobs=[example_job],
    resources={'s3': S3Resource(
                     region_name= 'us-east-1',
                     endpoint_url= 'http://myminio:9000',
                     aws_access_key_id= "test",
                     aws_secret_access_key= "r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G"

                                )}
)