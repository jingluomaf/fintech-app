#!/bin/bash
set -e # exit if a command exits with a not-zero exit code

POSTGRES="psql --username postgres"

# create a role for api
echo "Creating database role: api"
$POSTGRES <<-EOSQL
CREATE USER api WITH
    LOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    NOINHERIT
    NOREPLICATION
    PASSWORD 'api';
EOSQL