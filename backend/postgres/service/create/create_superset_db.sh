#!/bin/bash
set -e # exit immediately if a command exits with a non-zero status.

POSTGRES="psql --username ${POSTGRES_USER}"

# create database for superset
echo "Creating database: ${SUPERSET_DB}"
$POSTGRES <<EOSQL
CREATE DATABASE $SUPERSET_DB OWNER $SUPERSET_USER;
EOSQL