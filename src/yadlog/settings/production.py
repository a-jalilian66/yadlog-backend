from .common import *

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")

CSRF_TRUSTED_ORIGINS = os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")

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

STATIC_ROOT = os.path.join(BASE_DIR.parent, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR.parent, "media")

# STATIC_ROOT = "/app/staticfiles"
# MEDIA_ROOT = "/app/media"
