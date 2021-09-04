from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views


app_name = "users"
urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/", auth_views.LoginView.as_view(
            template_name="users/login.html"),
        name="login"
    ),
    path("account/", views.account, name="account"),
    path(
        "logout/", auth_views.LogoutView.as_view(
            template_name="users/logout.html"),
        name="logout"
    ),
    # RESET PASSWORD
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy('users:password_reset_done')),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('users:password_reset_complete'),
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
