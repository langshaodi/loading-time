"""
Django settings for core project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = BASE_DIR

# Load dotenv
import dotenv
dotenv.read_dotenv()
ENV = os.environ.get

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV("SECRET_KEY", None)

# Site ID
SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if ENV("DEBUG") in ["True", "true", "yes", "on"] else False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
    'puzzles',
    'games',
    'responses',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# URL Configuration

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   ENV("default_ENGINE",   ""),
        'NAME':     ENV("default_NAME",     ""),
        'USER':     ENV("default_USER",     ""),
        'PASSWORD': ENV("default_PASSWORD", ""),
        'HOST':     ENV("default_HOST",     ""),
        'PORT':     ENV("default_PORT",     ""),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

BUILD_ROOT  = os.path.join(BASE_DIR, 'dist/build/')

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'dist/static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  "dist/bower/"),
    BUILD_ROOT,
)

MEDIA_URL   = '/media/'
MEDIA_ROOT  = os.path.join(BASE_DIR, 'dist/media/')

# TEST SETTINGS
DELAY_LOWER_BOUND = int(ENV('DELAY_LOWER_BOUND', 0))
DELAY_UPPER_BOUND = int(ENV('DELAY_UPPER_BOUND', 100))

NUM_OF_PUZZLES = ENV('NUM_OF_PUZZLES', 10)
