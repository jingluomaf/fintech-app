#!/bin/bash
set -e # exit if a command exits with a not-zero exit code
set -a 
#Here put all the variables that will be marked for export
POSTGRES_USER="postgres"

AIRFLOW_USER="airflow"
AIRFLOW_PASSWORD="airflow"
AIRFLOW_DB="airflow"
set +a

/docker-entrypoint-initdb.d/create/create_airflow_user.sh
/docker-entrypoint-initdb.d/create/create_airflow_db.sh