#!/bin/bash
set -e # exit immediately if a command exits with a non-zero status.

POSTGRES="psql --username ${POSTGRES_USER}"

# create database for superset
echo "Creating database: ${AIRFLOW_DB}"
$POSTGRES <<EOSQL
CREATE DATABASE $AIRFLOW_DB OWNER $AIRFLOW_USER;
EOSQL