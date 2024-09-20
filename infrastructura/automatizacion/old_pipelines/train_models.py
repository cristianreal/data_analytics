from dagster import graph,job, op, Definitions,OpExecutionContext
from dagster_aws.s3 import S3Resource
from dagster_shell import execute_shell_command
import logging
from utils import download_files,upload_files


@op
def create_temp_folders(context: OpExecutionContext):
    lgr = logging.getLogger('console_logger')
    lgr.error("Creating folders")
    execute_shell_command('mkdir -p /opt/training_data && mkdir -p /opt/training_performance && mkdir -p /opt/models  && mkdir -p /opt/training_performance_mejorado && mkdir -p /opt/models_mejorado', output_logging="STREAM", log=context.log)
    execute_shell_command('rm -rf /opt/models/*', output_logging="STREAM", log=context.log)
    return None

@op
def download_data(context: OpExecutionContext,object_input):
    download_files("training_data/","/opt/")
    # Validate which files were downloaded
    execute_shell_command('ls -al /opt/training_data', output_logging="STREAM", log=context.log)
    return None

def run_random_forest(context, input_data, training_name, lista_clientes):
  output_folder='/opt/training_performance'
  output_modelos='/opt/models'
  knime_path='/opt/binaries/knime_4.7.5/knime'
  knime_workflow='/opt/knime_scripts/Modelo_Gradient_Boosted_cat_log.knwf'
  # Validate which files were downloaded
  execute_shell_command(f"{knime_path} --launcher.suppressErrors -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION  -workflowFile=\"{knime_workflow}\" \
      -workflow.variable=input_data,{input_data},String \
      -workflow.variable=output_folder,\"{output_folder}\",String \
      -workflow.variable=output_modelos,\"{output_modelos}\",String \
      -workflow.variable=training_name,\"{training_name}\",String \
      -workflow.variable=lista_clientes,\"{lista_clientes}\",String", output_logging="STREAM", log=context.log)

def run_random_forest_mejorado(context, input_data, training_name, lista_clientes):
  output_folder='/opt/training_performance_mejorado'
  output_modelos='/opt/models_mejorado'
  knime_path='/opt/binaries/knime_4.7.5/knime'
  knime_workflow='/opt/knime_scripts/Modelo_Gradient_Boosted_cat_log_mejorado.knwf'
  # Validate which files were downloaded
  execute_shell_command(f"{knime_path} --launcher.suppressErrors -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION  -workflowFile=\"{knime_workflow}\" \
      -workflow.variable=input_data,{input_data},String \
      -workflow.variable=output_folder,\"{output_folder}\",String \
      -workflow.variable=output_modelos,\"{output_modelos}\",String \
      -workflow.variable=training_name,\"{training_name}\",String \
      -workflow.variable=lista_clientes,\"{lista_clientes}\",String", output_logging="STREAM", log=context.log)


@op
def execute_knime_workflow_random_forest(context: OpExecutionContext,object_input):
    run_random_forest(context, '/opt/training_data/dataset_variables_cat_log.txt','cat_log','C00508')
    run_random_forest(context, '/opt/training_data/data-2022.txt','cat_log_2022','C00508')
    ### Mejorado
    run_random_forest_mejorado(context, '/opt/training_data/dataset_variables_cat_log.txt','cat_log_mejorado','C00508')
    run_random_forest_mejorado(context, '/opt/training_data/data-2022.txt','cat_log_mejorado_2022','C00508')
    return None

@op
def upload_data(context: OpExecutionContext,object_input):
    execute_shell_command(f"ls -al /opt/models/", output_logging="STREAM", log=context.log)
    upload_files("/opt/models/","models")
    upload_files("/opt/models_mejorado/","models")
    execute_shell_command(f"ls -al /opt/training_performance/", output_logging="STREAM", log=context.log)
    upload_files("/opt/training_performance/","training_performance")
    upload_files("/opt/training_performance_mejorado/","training_performance")
    return None

@job
def train_models():
  t0 = create_temp_folders()
  t1=download_data(t0)
  t2 = execute_knime_workflow_random_forest(t1)
  t3 = upload_data(t2)


defs = Definitions(
    jobs=[train_models],
    resources={'s3': S3Resource(
                     region_name= 'us-east-1',
                     endpoint_url= 'http://myminio:9000',
                     aws_access_key_id= "test",
                     aws_secret_access_key= "r2X+g+cvrpVlJ2Eqcb8bjelI2AIPbiF2YszEs72G"

                                )}
)