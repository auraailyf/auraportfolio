"""
Django settings for auraportfolio project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ===================== SECURITY =====================
SECRET_KEY = 'django-insecure-o#7qc+^j#!=6&+$2a2$$k*4^qch9q_m=4v)at_ur+i%^hn^#7c'

DEBUG = False# Turn off debug in production

ALLOWED_HOSTS = ['auraportfolio.onrender.com', 'localhost', '127.0.0.1']


# ===================== APPLICATIONS =====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]


# ===================== MIDDLEWARE =====================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # Whitenoise for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ===================== URLS & WSGI =====================
ROOT_URLCONF = 'auraportfolio.urls'
WSGI_APPLICATION = 'auraportfolio.wsgi.application'


# ===================== TEMPLATES =====================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


# ===================== DATABASE =====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===================== PASSWORD VALIDATION =====================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ===================== INTERNATIONALIZATION =====================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ===================== STATIC FILES =====================
STATIC_URL = '/static/'

# Where Django will look for your app static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Where collectstatic will put all files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Enable compressed static file storage (for Whitenoise)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# ===================== DEFAULT PRIMARY KEY =====================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ===================== EMAIL CONFIG =====================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'auraailyf@gmail.com'
EMAIL_HOST_PASSWORD = 'fyigygzgeaznfgil'   # Gmail app password
