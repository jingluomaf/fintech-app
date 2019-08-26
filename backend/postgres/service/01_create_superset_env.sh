#!/bin/bash
set -e # exit if a command exits with a not-zero exit code
set -a 
#Here put all the variables that will be marked for export
POSTGRES_USER="postgres"

SUPERSET_USER="superset"
SUPERSET_PASSWORD="superset"
SUPERSET_DB="superset"
set +a

/docker-entrypoint-initdb.d/create/create_superset_user.sh
/docker-entrypoint-initdb.d/create/create_superset_db.sh