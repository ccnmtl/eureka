import sys
from eureka.settings_shared import *  # noqa F403
from ctlsettings.staging import common
from django.conf import settings
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

locals().update(
    common(
        project=project,  # noqa f405
        base=base,  # noqa f405
        STATIC_ROOT=STATIC_ROOT,  # noqa f405
        INSTALLED_APPS=INSTALLED_APPS,  # noqa f405
        s3prefix="ccnmtl",
    ))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eureka',
        'HOST': '',
        'PORT': '6432',
        'USER': '',
        'PASSWORD': '',
    }
}

try:
    from eureka.local_settings import *  # noqa f403
except ImportError:
    pass

if ('migrate' not in sys.argv) and \
   ('collectstatic' not in sys.argv) and \
   hasattr(settings, 'SENTRY_DSN'):
    sentry_sdk.init(
        dsn=SENTRY_DSN,  # noqa F405
        integrations=[DjangoIntegration()],
        debug=True,
    )
