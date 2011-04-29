DEBUG = False
SECRET_KEY = 'KEEP_THIS_TO_YOURSELF'

ADMINS = (
    ('Joe Bloggs', 'jbloggs@example.com'),
)

LANGUAGES = [('en', 'en')]
DEFAULT_LANGUAGE = 0

DB_ENGINE = 'django.db.backends.mysql'
DB_NAME = 'dddm'
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_PORT = ''

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-GB'

SITE_ID = 1

MEDIA_ROOT = '/var/projects/dddm/media/'
MEDIA_URL = '/media/'
STATIC_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_DIRS = (
    '/var/projects/dddm/template',
)