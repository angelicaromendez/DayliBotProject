# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000

CMD ["/bin/bash", "-c", "\
    echo 'Aplicando migraciones...' && \
    python manage.py migrate && \
    echo 'Creando superusuario...' && \
    python manage.py createsuperuser --noinput \
      --username $DJANGO_SUPERUSER_USERNAME \
      --email $DJANGO_SUPERUSER_EMAIL || true && \
    echo 'Iniciando Gunicorn...' && \
    gunicorn --bind 0.0.0.0:$PORT DayliBot.wsgi:application"]