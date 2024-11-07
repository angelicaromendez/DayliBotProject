# Dockerfile para Django
FROM python:3.10-alpine

# Instalar las dependencias necesarias
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

WORKDIR /app

# Copia el archivo de dependencias y las instala
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación Django al contenedor
COPY . /app/

# Expone el puerto que usará Django (normalmente el 8000)
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
