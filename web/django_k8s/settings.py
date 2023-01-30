"""
Django settings for django_k8s project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR / "django_k8s"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "1"

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    str(os.environ.get("ALLOWED_HOST_IP")),
    str(os.environ.get("ALLOWED_HOST_WWW")),
    str(os.environ.get("ALLOWED_HOST_DOMAIN")),
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'django_k8s.apps.accounts',
    'django_k8s.apps.public',
    'django_k8s.apps.contact',
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_k8s.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / "templates"],
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

WSGI_APPLICATION = 'django_k8s.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAIL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])
DB_IGNORE_SSL = os.environ.get("DB_IGNORE_SSL") == "true"

if DB_IS_AVAIL:

    DATABASES = {
        "default": {
            "ENGINE": 'django.db.backends.postgresql',
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT
        }
    }
    
    if not DB_IGNORE_SSL:
        DATABASES["default"]["OPTIONS"] = {
            'sslmode': "require"
        }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# For deployment
STATIC_ROOT = BASE_DIR / "staticfiles-cdn"

# For development
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]
if DEBUG==False:
    from .cdn.conf import * # noqa

LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "public:index"
LOGOUT_REDIRECT_URL = "public:index"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "charlie.james.bell@gmail.com"

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_HOST_PASSWORD'))
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CORS_ALLOWED_ORIGINS = [
    "https://fra1.digitaloceanspaces.com",
    "http://" + str(os.environ.get("ALLOWED_HOST_IP")),
    "http://" + str(os.environ.get("ALLOWED_HOST_WWW")),
    "http://" + str(os.environ.get("ALLOWED_HOST_DOMAIN")),
]

CORS_ALLOW_METHODS = [
    "GET",
]

CORS_ALLOW_HEADERS = [
    "origin",
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

ADMINS = [('Me', 'charlie.james.bell@gmail.com')]