from .base_settings import *


DEBUG = True

STATICFILES_DIRS = [BASE_DIR / "static"]

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / config("DB_URL"),
    }
}
