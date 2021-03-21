from users.views import (UserSignUpView, UserProfileView,
                         ListCreateOrganizationsAPIView, OrganizationProfileGetView,
                         OrganizationUsersAPIView, ListAllUsersAPIView, activate)
from django.urls import path, re_path

app_name = 'users'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup-api'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate-user'),
    path('user/', UserProfileView.as_view(), name='user-retrieve-update-destroy-api'),
    path('users/all/', ListAllUsersAPIView.as_view(), name='list-all-users-api'),
    path('organizations/', ListCreateOrganizationsAPIView.as_view(), name='list-create-org'),
    path('organizations/users/', OrganizationUsersAPIView.as_view(), name='org-users'),
    path('organization/<int:pk>/detail/', OrganizationProfileGetView.as_view(), name='org-retrieve-api'),
]