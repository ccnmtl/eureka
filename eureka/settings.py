# flake8: noqa
from eureka.settings_shared import *

try:
    from eureka.local_settings import *
except ImportError:
    pass
