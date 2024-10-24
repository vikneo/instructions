"""
Django settings for documents project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

from utils.log_config import LevelFileHandler

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "adsasdaad56a7")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", 1)

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1").split()
INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "debug_toolbar",
    'users.apps.UsersConfig',
    'instruction.apps.InstructionConfig',
    # 'manuals.apps.ManualsConfig',
    "import_export",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'documents.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'documents.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE_SQL", "django.db.backends.sqlite3"),
        'NAME': BASE_DIR / os.getenv("NAME_SQL", "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

LOCAL_MACHINE_DEV = os.getenv("LOCAL_MACHINE_DEV") == "1"

# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# cachings

CACHE_ROOT = os.path.join(BASE_DIR, "cache")
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": CACHE_ROOT,
        "TIMEOUT": 60 * 60 * 24,
    }
}

CACHE_NAME_INSTRUCT = 'instructions'
CACHE_NAME_PROJECT = 'products'

# sessions

SESSION_COOKIE_AGE = 14 * 24 * 60 * 60

SESSION_EXPIRE_AT_CLOSE = True

# Loging

LOGIN_REDIRECT_URL = ''

LOGGING_ROOT = BASE_DIR / "logging"
LOGGING_URL = "/logging/"

LOGFILE_NAME = "loging.log"

LOGFILE_SIZE = 2 * 1024 * 1024  # size 2.6 Mb
LOGFILE_COUNT = 10

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base': {
            'format': '%(asctime)s [%(levelname)s] "%(name)s : %(lineno)s : %(message)s"'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'base',
            'stream': 'ext://sys.stdout',
        },
        'file_log': {
            "class": "logging.handlers.RotatingFileHandler",
            'level': 'INFO',
            'formatter': 'base',
            'filename': os.path.join(LOGGING_ROOT, LOGFILE_NAME),
            'maxBytes': LOGFILE_SIZE,
            'backupCount': LOGFILE_COUNT,
            'mode': 'a',
            'encoding': 'utf-8'
        },
        "file_by_date": {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'base',
            'filename': os.path.join(LOGGING_ROOT, LOGFILE_NAME),
            'when': 'D',
            'backupCount': LOGFILE_COUNT,
            'encoding': 'utf-8'

        },
        "custom_file_log": {
            "()": LevelFileHandler,
            'level': 'INFO',
            'formatter': 'base',
            'filename': os.path.join(LOGGING_ROOT, LOGFILE_NAME),
            'maxBytes': LOGFILE_SIZE,
            'backupCount': LOGFILE_COUNT,
            'mode': 'a',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'root': {
            'level': 'INFO',
            'handlers': ['console', 'custom_file_log']
        },
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
