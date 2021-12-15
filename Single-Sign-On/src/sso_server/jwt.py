from services.models import Service
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['aud'] = []
        user_services = Service.for_user(user)
        for service in user_services:
            token['aud'].append(service.identifier)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'email': self.user.email})
        data.update({'first_name': self.user.first_name})
        data.update({'last_name': self.user.last_name})
        return data
# A JWT access-token example
#
# {
#     'token_type': 'access',
#     'exp': 1599980514,
#     'jti': 'a3c77262a57d4df5a657fe12860c8492',
#     'user_id': '9a7b69e2-df4d-4c98-bc04-941c66cff1a0',
#     'aud': ['Docs', 'Sheets']
# }
#

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
