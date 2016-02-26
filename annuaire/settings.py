"""
Django settings for annuaire project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yi0cvdox+5vre4ny&k8up_*7sj$ylnqe-uqcu$b85w&%dk%9e6'

if socket.gethostname() == 'MacBook-Air-de-Vincent.local':
    DEBUG = True
else:
    DEBUG = False

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'app.pipelines.save_profile_picture' #save facebook profile image
)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'stormy-citadel-1861.herokuapp.com', 'consocollaborative.com', 'annuaire.consocollaborative.com']

ADMINS = [('Vincent', 'vincent.poulain2@gmail.com')]

# Application definition

INSTALLED_APPS = (
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    's3direct',
    'djangobower',
    'vote',
    'sass_processor'
)

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = 'annuaire-consocollab'

S3DIRECT_REGION = 'eu-west-1'

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'annuaire.urls'

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
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'annuaire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'annuaire',
        'USER': 'admin',
        'PASSWORD': 'size',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
         'PORT': '',                      # Set to empty string for default.
    }
}

if socket.gethostname() != 'MacBook-Air-de-Vincent.local':
    DATABASES['default'] = dj_database_url.config()


S3DIRECT_DESTINATIONS = {
    # Allow anybody to upload jpeg's and png's.
    'imgs': ('uploads/imgs', lambda u: True, ['image/jpeg', 'image/jpg', 'image/png'],)
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'app', 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'root') 

STATICFILES_FINDERS = ('djangobower.finders.BowerFinder', 'django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder')

BOWER_COMPONENTS_ROOT = BASE_DIR + '/components/'

BOWER_INSTALLED_APPS = (
    'jquery#1.9',
    'underscore',
    'gridism'
)

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

