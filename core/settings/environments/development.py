from core.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "debug_toolbar"
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]
INTERNAL_IPS = [
    "127.0.0.1",
]