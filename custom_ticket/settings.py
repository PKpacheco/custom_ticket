"""
Django settings for custom_ticket project.
Generated by 'django-admin startproject' using Django 1.11.11.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import dj_database_url
import os
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't6id7sj_w*wt%bu+wc!g-4&(q4_9hp6-mwn+zp)5aota3n0)g+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1', '.herokuapp.com']


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'events',
    'mail',
    'customizations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

    # El siguiente middleware, lanza el Error:
    # django.core.exceptions.ImproperlyConfigured:
    # WSGI application 'custom_ticket.wsgi.application'
    # could not be loaded; Error importing module:
    # 'No module named social.apps.django_app.middleware'

    'custom_ticket.middleware.SocialAuthExceptionMiddleware',

]


ROOT_URLCONF = 'custom_ticket.urls'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)


AUTHENTICATION_BACKENDS = (
    'social_core.backends.eventbrite.EventbriteOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_EVENTBRITE_KEY = get_env_variable('SOCIAL_AUTH_EVENTBRITE_KEY')
SOCIAL_AUTH_EVENTBRITE_SECRET = get_env_variable('SOCIAL_AUTH_EVENTBRITE_SECRET')
SERVER_ACCESS_TOKEN = get_env_variable('SERVER_ACCESS_TOKEN')


WSGI_APPLICATION = 'custom_ticket.wsgi.application'

# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'djangogirls',
#         'USER': 'name',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator',
        )
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

# Email config

EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_PORT = int(get_env_variable('EMAIL_PORT'))
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = bool(get_env_variable('EMAIL_USE_TLS'))

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Mendoza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}
