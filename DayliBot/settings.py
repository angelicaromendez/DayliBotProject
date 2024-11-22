import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.getenv('SECRET_KEY', 'default-unsafe-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'Bot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DayliBot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DayliBot.wsgi.application'

# Database configuration using environment variables
if os.getenv("DOCKERIZED") == "true":
    # Configuración específica para Docker
    DATABASES = {
     'default': dj_database_url.config(
        conn_max_age=600,
    )

}
else:
    # Configuración general o para desarrollo local
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv(
                "DATABASE_URL",
                "postgres://user:password@localhost:5432/dbname"
            ),
            conn_max_age=600,
        )
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Define la URL base para los archivos estáticos
STATIC_URL = '/static/'

# Define el directorio donde Django almacenará los archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Si quieres servir archivos estáticos adicionales desde un directorio de tu elección:
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Si tienes archivos estáticos adicionales en la carpeta 'static'
]
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
