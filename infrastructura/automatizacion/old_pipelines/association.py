from dagster import graph,job, op, Definitions,OpExecutionContext
from dagster_aws.s3 import S3Resource
from dagster_shell import execute_shell_command
import logging



@op
def execute_knime_workflow_association(context: OpExecutionContext):
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

@job
def run_association_rules():
  execute_knime_workflow_association()

defs = Definitions(
    jobs=[run_association_rules],
    resources={'s3': S3Resource(
                     region_name= 'us-east-1',
                     endpoint_url= 'http://myminio:9000',
                     aws_access_key_id= "test",
                     aws_secret_access_key= "r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G"

                                )}
)