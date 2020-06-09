# flake8: noqa
from sprezzatura.settings_shared import *

try:
    from sprezzatura.local_settings import *
except ImportError:
    pass
