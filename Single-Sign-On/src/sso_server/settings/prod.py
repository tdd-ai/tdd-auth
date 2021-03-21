from .base import *

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

DATABASES = {
	"default": {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv('DATABASE_NAME', 'postgres'),
    'USER': os.getenv('DATABASE_USERNAME', 'postgres'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD', 'postgres'),
    'HOST': os.getenv('DATABASE_HOST', 'db'),
    'PORT': os.getenv('DATABASE_PORT', 5432),
	}
}

INTERNAL_IPS = ["localhost", "127.0.0.1"]

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = BASE_DIR / "static/"

# Email setting
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', None)
EMAIL_HOST = os.getenv('EMAIL_HOST', None)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', None)
EMAIL_PORT = os.getenv('EMAIL_PORT', None)