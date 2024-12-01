from .base_settings import *


DEBUG = False
ALLOWED_HOSTS = ["*"]

STATIC_ROOT = BASE_DIR / "staticcdn"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / config("DB_URL"),
    }
}

