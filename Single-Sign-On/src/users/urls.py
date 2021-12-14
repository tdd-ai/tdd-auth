from users.views import (UserSignUpView, UserProfileView,
                         ListCreateOrganizationsAPIView, OrganizationProfileGetView,
                         OrganizationUsersAPIView, ListAllUsersAPIView, activate)
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'users'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup-api'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate-user'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html", email_template_name='users/password_reset_email.html', success_url="done/"), name='reset_password'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html", success_url="password-reset-complete/"), name="password_reset_confirm"),
    path('password-reset-confirm/<uidb64>/set-password/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
    path('user/', UserProfileView.as_view(), name='user-retrieve-update-destroy-api'),
    path('users/all/', ListAllUsersAPIView.as_view(), name='list-all-users-api'),
    path('organizations/', ListCreateOrganizationsAPIView.as_view(), name='list-create-org'),
    path('organizations/users/', OrganizationUsersAPIView.as_view(), name='org-users'),
    path('organization/<int:pk>/detail/', OrganizationProfileGetView.as_view(), name='org-retrieve-api'),
]