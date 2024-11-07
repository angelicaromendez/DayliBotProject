#!/bin/bash
set -e

echo "Creating standard user and database if they don't already exist..."

# Crear usuario si no existe
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    DO
    \$do\$
    BEGIN
        IF NOT EXISTS (
            SELECT FROM pg_catalog.pg_roles
            WHERE rolname = '${DAYLI_BOT_USER}') THEN
            CREATE ROLE ${DAYLI_BOT_USER} WITH LOGIN PASSWORD '${DAYLI_BOT_PASSWORD}';
        END IF;
    END
    \$do\$;
EOSQL

# Crear base de datos si no existe
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    DO
    \$do\$
    BEGIN
        IF NOT EXISTS (
            SELECT FROM pg_database
            WHERE datname = '${DAYLI_BOT_DB}') THEN
            CREATE DATABASE ${DAYLI_BOT_DB} OWNER ${DAYLI_BOT_USER};
        END IF;
    END
    \$do\$;
EOSQL

echo "Initialization script completed successfully."
