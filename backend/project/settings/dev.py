from .base import *

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(' ')
