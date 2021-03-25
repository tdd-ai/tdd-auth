import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured

SSO_HOST_EMAIL = os.environ.get('SSO_HOST_EMAIL')
if not SSO_HOST_EMAIL:
    raise ImproperlyConfigured("'SSO_HOST_EMAIL' environment variable is unset")

SSO_HOST_PASSWORD = os.environ.get('SSO_HOST_PASSWORD')
if not SSO_HOST_PASSWORD:
    raise ImproperlyConfigured("'SSO_HOST_PASSWORD' environment variable is unset")

User = get_user_model()

help_message = f"""
Sets up the DB, creating:
1) superuser with admin rights (Email: {SSO_HOST_EMAIL})
"""

class Command(BaseCommand):
    """
    admin_setup: Command to set-up database for the application
    """
    help = help_message

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email=SSO_HOST_EMAIL).exists():
            User.objects.create_superuser(first_name="SSO ADMIN",
                                          email=SSO_HOST_EMAIL,
                                          password=SSO_HOST_PASSWORD)
            print('Super-User Created!')
