from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Organization

User = get_user_model()


class PublicOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'name',)


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class PublicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'avatar', 'email', 'nickname', 'affiliation',
                  'first_name', 'last_name',)


class UserSerializer(serializers.ModelSerializer):

    is_sso_admin = serializers.ReadOnlyField(source='is_staff')
    admin_org = OrganizationSerializer()
    organization = PublicOrganizationSerializer()

    class Meta:
        model = User
        fields = ('id', 'avatar', 'email', 'nickname',
                  'first_name', 'last_name', 'affiliation',
                  'admin_org', 'organization', 'is_sso_admin', 'is_staff')
        read_only_fields = ('admin_org', 'organization', 'is_staff')


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('avatar', 'email', 'nickname', 'affiliation',
                  'first_name', 'last_name', 'password')

    def validate_password(self, value):
        validate_password(value)
        return value
