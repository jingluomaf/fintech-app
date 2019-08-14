#!/bin/bash
set -e # exit immediately if a command exits with a non-zero status.

POSTGRES="psql --username postgres"

# create database for api
echo "Creating database: api"
$POSTGRES <<EOSQL
CREATE DATABASE api OWNER api;
EOSQL