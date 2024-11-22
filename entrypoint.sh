#!/bin/bash

set -e  # Termina el script si ocurre un error

echo "Aplicando migraciones..."
python manage.py migrate

echo "Creando superusuario..."
python manage.py createsuperuser --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true

echo "Iniciando Gunicorn..."
gunicorn --bind 0.0.0.0:"$PORT" DayliBot.wsgi:application