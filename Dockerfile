# Usa una imagen base de Python 3.9 o superior
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos de la aplicación al contenedor
COPY . .

# Asegúrate de que entrypoint.sh es ejecutable
RUN chmod +x entrypoint.sh

# Expone el puerto 8000 para el servidor
EXPOSE 8000

# Establece la variable de entorno para el puerto
ENV PORT 8000

# Usa el script de entrada como punto de entrada
ENTRYPOINT ["./entrypoint.sh"]