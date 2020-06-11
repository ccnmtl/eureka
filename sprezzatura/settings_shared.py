# Django settings for the Sprezzatura project.
import os.path
from ccnmtlsettings.shared import common

project = 'sprezzatura'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'sprezzatura.main',
]

USE_TZ = True

MIDDLEWARE += [  # noqa
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

INSTALLED_APPS += [  # noqa
    'bootstrap4',
    'infranil',
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

    'sprezzatura.main',
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
                'djangowind.context.context_processor',
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

WAGTAIL_SITE_NAME = 'Sprezzatura'
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

WIND_AFFIL_HANDLERS = ['sprezzatura.main.auth.WagtailEditorMapper',
                       'djangowind.auth.StaffMapper',
                       'djangowind.auth.SuperuserMapper']

WAGTAILADMIN_STATIC_FILE_VERSION_STRINGS = True
