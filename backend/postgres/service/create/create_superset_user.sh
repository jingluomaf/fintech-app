#!/bin/bash
set -e # exit if a command exits with a not-zero exit code

POSTGRES="psql -U ${POSTGRES_USER}"

# create a role for superset
echo "Creating database role: ${SUPERSET_USER}"
$POSTGRES <<-EOSQL
CREATE USER $SUPERSET_USER WITH
    LOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    NOINHERIT
    NOREPLICATION
    PASSWORD '$SUPERSET_PASSWORD';
EOSQL