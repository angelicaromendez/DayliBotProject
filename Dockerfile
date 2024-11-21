# Usa una imagen base de Python 3.9 o superior
FROM python:3.9-slim

# Instala el cliente de PostgreSQL para usar pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto 8000 para el servidor de Django
EXPOSE 8001

# Comando por defecto para correr el servidor de Django
#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8001"]
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "DayliBot.wsgi:application"]