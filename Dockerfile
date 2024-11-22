FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000

# Cambiar CMD para ejecutar migraciones y crear superusuario
CMD ["/bin/bash", "-c", "\
    echo 'Applying migrations...' && \
    python manage.py migrate && \
    echo 'Creating superuser...' && \
    python manage.py createsuperuser --noinput \
      --username $DJANGO_SUPERUSER_USERNAME \
      --email $DJANGO_SUPERUSER_EMAIL || true && \
    echo 'Starting Gunicorn...' && \
    gunicorn --bind 0.0.0.0:$PORT DayliBot.wsgi:application"]