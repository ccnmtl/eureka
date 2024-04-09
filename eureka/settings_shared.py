# Django settings for the Eureka project.
import os.path
import sys
from ctlsettings.shared import common

project = 'eureka'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'eureka.main',
]

USE_TZ = True

MIDDLEWARE += [  # noqa
    'django_cas_ng.middleware.CASMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

INSTALLED_APPS += [  # noqa
    'bootstrap4',
    'django_extensions',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.styleguide',
    'wagtail.contrib.table_block',
    'wagtail.contrib.modeladmin',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
    'wagtailfontawesome',
    'wagtailmenus',

    'eureka.main',
]

# Customized from CCNMTL Common
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(base, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'stagingcontext.staging_processor',
                'gacontext.ga_processor',
                'wagtail.contrib.settings.context_processors.settings',
                'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/cms/"

WAGTAIL_SITE_NAME = 'Eureka'
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

WAGTAILADMIN_STATIC_FILE_VERSION_STRINGS = True

WAGTAILMENUS_ACTIVE_ANCESTOR_CLASS = 'active'

# Set custom test runner
TEST_RUNNER = 'eureka.main.tests.runner.EurekaTestRunner'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Needed to get Cypress to run
if 'integrationserver' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            'HOST': '',
            'PORT': '',
            'USER': '',
            'PASSWORD': '',
            'ATOMIC_REQUESTS': True,
        }
    }
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )
