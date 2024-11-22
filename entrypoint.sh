#!/bin/bash

set -e

echo "Checking DATABASE_URL..."
if [ -z "$DATABASE_URL" ]; then
  echo "Error: DATABASE_URL is not set."
  exit 1
else
  echo "DATABASE_URL is set."
fi

echo "Applying migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py createsuperuser --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:"$PORT" DayliBot.wsgi:application