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

# Final path for collectstatic
STATIC_ROOT = BASE_DIR.parent / "staticfiles"

# Path to uploaded files
MEDIA_ROOT = BASE_DIR.parent / "media"

# We are going to collect static files from these paths.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'frontend', 'dist'),  # Tailwind build output
    os.path.join(BASE_DIR, 'static'),  # manually written static files
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
