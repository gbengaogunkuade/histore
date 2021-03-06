"""
Django settings for HiStore project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages   # messages alert
import environ  # environment variable

import django_heroku # new line (heroku)


# initialize the environment variable
env = environ.Env()

# read the .env file
environ.Env.read_env()




# messages alert tags and css styling
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary py-3',
        messages.INFO: 'alert-info py-3',
        messages.SUCCESS: 'alert-success py-3',
        messages.WARNING: 'alert-warning py-3',
        messages.ERROR: 'alert-danger py-3',       
}





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


TEMPLATES_DIR_1 = BASE_DIR / 'product/templates'
TEMPLATES_DIR_2 = BASE_DIR / 'visitor/templates'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env("SECRET_KEY")



# new line (heroku)
# --------------------------------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# new line (heroku)
# --------------------------------------------------------
ALLOWED_HOSTS = ['ogunkuadehistore.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product',
    'visitor',
    'django.contrib.humanize',       # for adding "human touch" to templates
    'django_countries',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',           # new line (heroku)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HiStore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR_1, TEMPLATES_DIR_2,],
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

WSGI_APPLICATION = 'HiStore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# new line (heroku)
# --------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DATABASE_NAME"),                   # database name
        'USER': env("DATABASE_USER"),                   # database user
        'PASSWORD': env("DATABASE_PASSWORD"),           # database password
        'HOST': '127.0.0.1',                            # database host
        'PORT': '5432',                                 # database port
    }
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


# new line (heroku)
# --------------------------------------------------------
STATIC_URL = '/static/'                         

STATICFILES_DIRS = [BASE_DIR / 'static']       

STATIC_ROOT = BASE_DIR / 'static_root'       

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 



# DEFINING THE MEDIA FILES URL
MEDIA_URL = '/media/'


# DEFINING THE MEDIA FILES LOCATION
MEDIA_ROOT = BASE_DIR / 'media'



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# DEFINE THE LOGIN URL FOR PAGES WITH "@login_required" SET ON THEM
LOGIN_URL = 'login_to_continue'         # IF THE USER IS NOT LOGGED IN, REDIRECT THE USER HERE



# # DEFINING THE LOGIN REDIRECT PATH
# LOGIN_REDIRECT_URL = 'home'


# LOGOUT_REDIRECT_URL = 'login' # new



# config/settings.py
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"



# DEFINE MAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'HiStore Team <noreply@histore.com>'
EMAIL_HOST_USER = env("EMAIL_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")




# --------------------------------------------------------------------------------------------------------
# stripe

STRIPE_SECRET_KEY = env("STRIPE_KEY")

STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")

# --------------------------------------------------------------------------------------------------------



# new line (heroku)
# --------------------------------------------------------
import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)




# new line (heroku)
# --------------------------------------------------------
django_heroku.settings(locals())    # new line
