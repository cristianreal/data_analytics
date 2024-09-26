FROM python:3.12-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app
RUN apt-get update && apt-get install -y libxkbcommon-x11-0 libgbm-dev software-properties-common
RUN apt-get update && apt-get install -y openjdk-17-jdk
RUN pip install dagster dagster-webserver dagster-postgres dagster-aws dagster-shell pandas
RUN pip install psycopg2-binary python-dotenv pyarrow fastparquet pyspark
# Copy your code and workspace to /opt/dagster/app
#COPY repo.py workspace.yaml /opt/dagster/app/

ENV DAGSTER_HOME=/opt/dagster/dagster_home/

# Copy dagster instance YAML to $DAGSTER_HOME
COPY dagster.yaml /opt/dagster/dagster_home/

WORKDIR /opt/dagster/app

EXPOSE 3000

ENTRYPOINT ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]
