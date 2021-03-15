"""
Django settings for sso_server project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h83#*q+*4208r4=@*db%-7q#tl6wx$9e8+u6t*!#sk%!*9_g+s'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'users',
    'services',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'sso_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates/"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sso_server.wsgi.application'
AUTH_USER_MODEL = 'users.User'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CONFIG_DIR = os.path.join(Path(BASE_DIR).parent, 'config')
JWT_PRIVATE_KEY_PATH = os.path.join(CONFIG_DIR, 'jwt_key')
JWT_PUBLIC_KEY_PATH = os.path.join(CONFIG_DIR, 'jwt_key.pub')

if (not os.path.exists(JWT_PRIVATE_KEY_PATH)) or (not os.path.exists(JWT_PUBLIC_KEY_PATH)):

    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(JWT_PRIVATE_KEY_PATH, 'w') as pk:
        pk.write(pem.decode())

    public_key = private_key.public_key()
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(JWT_PUBLIC_KEY_PATH, 'w') as pk:
        pk.write(pem_public.decode())
    print('PUBLIC/PRIVATE keys Generated!')

# Visit this page to see all the registered JWT claims:
# https://tools.ietf.org/html/rfc7519#section-4.1
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # "exp" (Expiration Time) Claim
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # "exp" (Expiration Time) Claim

    'ALGORITHM': 'RS256',  # 'alg' (Algorithm Used) specified in header

    'SIGNING_KEY': open(JWT_PRIVATE_KEY_PATH).read(),
    'VERIFYING_KEY': open(JWT_PUBLIC_KEY_PATH).read(),

    'AUDIENCE': None,  # "aud" (Audience) Claim
    'ISSUER': None,  # "iss" (Issuer) Claim

    'USER_ID_CLAIM': 'user_id',  # The field name to use for identifying user
    'USER_ID_FIELD': 'id',  # The field in the DB which will be filled in USER_ID_CLAIM

    'JTI_CLAIM': 'jti',  # A token’s unique identifier

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ROTATE_REFRESH_TOKENS': False,
}

# A JWT access-token example
#
# {
#     'token_type': 'access',
#     'exp': 1599980514,
#     'jti': 'a3c77262a57d4df5a657fe12860c8492',
#     'user_id': '9a7b69e2-df4d-4c98-bc04-941c66cff1a0',
# }
#
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
