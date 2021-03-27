from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
	BASE_DIR / "static/"
]

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]


INTERNAL_IPS = ["localhost", "127.0.0.1"]
ALLOWED_HOSTS = ["*"]


# Mail address verification
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'