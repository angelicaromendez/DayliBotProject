#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    DO
    \$do\$
    BEGIN
        IF NOT EXISTS (
            SELECT FROM pg_catalog.pg_roles
            WHERE rolname = '${POSTGRES_USER}') THEN
            CREATE ROLE ${POSTGRES_USER} WITH LOGIN PASSWORD '${POSTGRES_PASSWORD}';
        END IF;
    END
    \$do\$;

    ALTER ROLE ${POSTGRES_USER} CREATEDB;
EOSQL
