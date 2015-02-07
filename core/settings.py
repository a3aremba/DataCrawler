# Django settings for pb_auth project.
import os.path
import socket
import dj_database_url


CFG_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(CFG_PATH, '..'))
rootDirName = os.path.split(ROOT_PATH)[1]
DEBUG = True
RELEASE = False
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

HOST_NAME = socket.gethostname()

ADMINS = (
    ('admin', 'a.3aremba@gmail.com'),
)

MANAGERS = ADMINS

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_HOST = 'localhost'
# SESSION_REDIS_PORT = 6379
# SESSION_REDIS_DB = 2
# SESSION_COOKIE_AGE = 60 * 60 * 3

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'
DATE_FORMAT = 'd F Y'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../media').replace('\\','/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static').replace('\\','/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"

STATIC_URL = '/static/'

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# SECRET_KEY = 'x3s7skmnx)kpjrn!m&amp;=(m4cy(ri#67g$gxgh%w6-0n@(@1tn%m'
SECRET_KEY = 'x3s7skmnx'
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'core.wsgi.application'

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'core/templates/'),
    os.path.join(PROJECT_DIR, 'crowler/templates/'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'core',
    'crowler',
)

# CACHES = {
#     "default": {
#         "BACKEND": "redis_cache.cache.RedisCache",
#         "LOCATION": "127.0.0.1:6379:1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "redis_cache.client.DefaultClient",
#         }
#     }
# }

LOGIN_URL ="/admin/"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'log_file_core':{
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOT_PATH, 'logs/core.log'),
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'simple'
        },
        'log_file_crowler':{
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOT_PATH, 'logs/crowler.log'),
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'simple'
        },
    },
    'loggers': {
        'core': {
            'handlers': ['log_file_core'],
            'level': 'INFO',
            'propagate': True,
        },
        'crowler': {
            'handlers': ['log_file_crowler'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# LOGGER_STATUS_CODE = [200, 300, 400, 500]
# LOGGER_REDIS_HOST = 'localhost'
# LOGGER_REDIS_PORT = 6379
# LOGGER_REDIS_DB = 0
# LOGGER_REDIS_LIST = 'corde-parel-log'
# LOGGER_UDP_HOST = 'log0.bpp.it.loc'
# LOGGER_UDP_PORT = 13200
# LOGGER_TO_FILE = 'core'

FEINCMS_USE_PAGE_ADMIN=False

try:
    from core.local_settings import *
except ImportError:
    pass