from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
    }
}

STATIC_ROOT = BASE_DIR.parent / "static"
MEDIA_ROOT = BASE_DIR.parent / "media"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'frontend', 'dist'),
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
