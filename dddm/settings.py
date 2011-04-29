# -*- coding: utf-8 -*-
import os
import localsettings

gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = localsettings.DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = localsettings.ADMINS

MANAGERS = ADMINS

LANGUAGES = localsettings.LANGUAGES
DEFAULT_LANGUAGE = localsettings.DEFAULT_LANGUAGE


DATABASES = {
    'default': {
        'ENGINE': localsettings.DB_ENGINE,  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': localsettings.DB_NAME,                      # Or path to database file if using sqlite3.
        'USER': localsettings.DB_USER,                      # Not used with sqlite3.
        'PASSWORD': localsettings.DB_PASSWORD,                  # Not used with sqlite3.
        'HOST': localsettings.DB_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': localsettings.DB_PORT,                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = localsettings.TIME_ZONE

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = localsettings.LANGUAGE_CODE

SITE_ID = localsettings.SITE_ID

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = localsettings.MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = localsettings.MEDIA_URL
STATIC_URL = localsettings.STATIC_URL

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = localsettings.ADMIN_MEDIA_PREFIX

# Make this unique, and don't share it with anybody.
SECRET_KEY = localsettings.SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
)

CMS_TEMPLATES = (
    ('index.html', 'Homepage'),
    ('agenda.html', 'Agenda'),
)

ROOT_URLCONF = 'dddm.urls'

AUTH_PROFILE_MODULE = 'account.UserProfile'

TEMPLATE_DIRS = localsettings.TEMPLATE_DIRS

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_extensions',
    'cms',
    'menus',
    'mptt',
    'appmedia',
    'south',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.googlemap',
    'dddm.account',
    'dddm.session',
)

CMS_SEO_FIELDS = True
