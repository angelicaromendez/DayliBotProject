# Usa una imagen base de Python 3.9 o superior
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto para el servidor de Django
EXPOSE 8000

# Establece la variable de entorno para el puerto
ENV PORT 8000

# Comando por defecto para correr Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py createsuperuser --no-input --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL && gunicorn --bind 0.0.0.0:$PORT DayliBot.wsgi:application"]