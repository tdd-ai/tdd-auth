from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from rest_framework import status
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveAPIView)
from rest_framework.permissions import (IsAuthenticated, SAFE_METHODS)
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Organization
from users.permissions import (IsOwner, IsOrganizationAdminOrSSOAdmin,
                               IsOrganizationAdmin, IsSSOAdminOrReadOnly)
from users.serializers import (CreateUserSerializer, UserSerializer,
                               OrganizationSerializer, PublicOrganizationSerializer,
                               PublicUserSerializer)

from .tokens import account_activation_token

User = get_user_model()


class ListCreateOrganizationsAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsSSOAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return PublicOrganizationSerializer
        else:
            return OrganizationSerializer

    def get_queryset(self):
        return Organization.objects.all()


class OrganizationUsersAPIView(ListAPIView):

    permission_classes = (IsAuthenticated, IsOrganizationAdmin,)
    serializer_class = PublicUserSerializer

    def get_queryset(self):
        request_user = self.request.user
        return request_user.admin_org.users.exclude(id=request_user.id)


class ListAllUsersAPIView(ListAPIView):
    serializer_class = PublicUserSerializer

    def get_queryset(self):
        request_user = self.request.user
        return User.objects.exclude(id=request_user.id)


class OrganizationProfileGetView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Organization.objects.all()

    def retrieve(self, request, *args, **kwargs):
        organization = self.get_object()
        serializer = PublicOrganizationSerializer(organization)
        if IsOrganizationAdminOrSSOAdmin().has_object_permission(request, self, organization):
            serializer = OrganizationSerializer(organization)
        return Response(serializer.data)


class UserProfileView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwner,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserSignUpView(APIView):

    def post(self, request, *args, **kwargs):
        serialized = CreateUserSerializer(data=request.data)
        if serialized.is_valid():
            
            serializer_data = serialized.validated_data

            user = User.objects.create_user(**serializer_data)
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request)
            mail_subject = 'Activate your account at %s' % current_site.domain
            
            message = render_to_string('users/email_template.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })

            to_email = serializer_data["email"]
            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

            return Response('Please confirm your email address to complete the registration', status=status.HTTP_201_CREATED)

        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response('Thank you for your email confirmation. Now you can login your account.')
    else:
        return Response('Activation link is invalid!')