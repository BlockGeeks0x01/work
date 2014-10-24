# Django settings for ucenter project.

import platform
import os
import logging

from lib.db_setting import USER_CENTER_DATABASE

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Harrison', 'sunguyu@123feng.com'),
)

MANAGERS = ADMINS

DATABASES = USER_CENTER_DATABASE

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

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
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7z1iv!43x5x89pxtuq=sxdtcxe28+d(1wkg2v)0i9tf6$&$8%8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'lib.middleware.AuthMiddleware',
    #'lib.middleware.LoggingMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'etc.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'etc.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'user_center.user_api',
    'raven.contrib.django.raven_compat',
    #'django_extensions',
)

DATABASE_ROUTERS = ['lib.db_setting.AtomRouter']

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGFILE_PATH = {
    "API": "/home/gezbox/Atom/log/user_center",
    "NEW-API": "/home/gezbox/Atom/log/user_center",
    "BOX-NEW": "/home/gezbox/Atom/log/user_center",
    "box-1": "/home/gezbox/Atom/log/user_center",
    "AY14072213291500867dZ": "/root/gezbox/Atom/user_center/log",
}.get(platform.node(), os.path.join(__file__[:__file__.rfind('etc/')],'log'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
         'standard': {
             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
             'datefmt' : "%d/%b/%Y %H:%M:%S"
         },
         'api': {
             'format' : "[%(asctime)s] %(levelname)s [%(funcName)s] %(message)s",
             'datefmt' : "%d/%b/%Y %H:%M:%S"
         },
         'data': {
             'format' : "[%(asctime)s] %(levelname)s %(message)s",
             'datefmt' : "%d/%b/%Y %H:%M:%S"
         },
     },
     'handlers': {
         'null': {
             'level':'DEBUG',
             'class':'django.utils.log.NullHandler',
         },
         'api_handler': {
             'level':'DEBUG',
             'class':'logging.handlers.RotatingFileHandler',
             'filename': "%s/api/%s" % (LOGFILE_PATH, "api.log"),
             'maxBytes': 50 * 1024 * 1024,
             'encoding': 'utf-8',
             'backupCount': 10,
             'formatter': 'api',
         },
         'data_handler': {
             'level': 'DEBUG',
             'class': 'logging.handlers.TimedRotatingFileHandler',
             'filename': "%s/data/%s" % (LOGFILE_PATH, "data.log"),
             'when': 'D',
             'encoding': 'utf-8',
             'formatter': 'data',
         },
         'console':{
             'level':'INFO',
             'class':'logging.StreamHandler',
             'formatter': 'standard'
         },
         'mail_admins': {
             'level': 'ERROR',
             'class': 'django.utils.log.AdminEmailHandler',
             'include_html': True
         },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'api_logger': {
            'handlers': ['console', 'api_handler'],
            'level': 'DEBUG',
        },
        'data_logger': {
            'handlers': ['console', 'data_handler'],
            'level': 'DEBUG',
        },
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False
        # },
    }
}

api_logger = logging.getLogger('api_logger')
data_logger = logging.getLogger('data_logger')

RAVEN_CONFIG = {
    'dsn': 'http://17442206e6554817a8a9ee2b34bda94b:1f5ed591be1d4d89a0b7ece746e84de2@127.0.0.1:9005/2',
}


EMAIL_HOST = "smtp.exmail.qq.com"
EMAIL_HOST_USER = "no-reply@123feng.com"
EMAIL_HOST_PASSWORD = r"wcl5iFGbV6Zl&"

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SEND_BROKEN_LINK_EMAILS = True