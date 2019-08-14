#!/bin/bash
set -e # exit if a command exits with a not-zero exit code

POSTGRES="psql -U ${POSTGRES_USER}"

# create a role for airflow
echo "Creating database role: ${AIRFLOW_USER}"
$POSTGRES <<-EOSQL
CREATE USER ${AIRFLOW_USER} WITH
    LOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    NOINHERIT
    NOREPLICATION
    PASSWORD '${AIRFLOW_PASSWORD}';
EOSQL