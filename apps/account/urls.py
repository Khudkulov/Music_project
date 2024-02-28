from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .form import MyPasswordResetForm
from .views import RegistrateView, LogoutView

app_name = 'account'

urlpatterns = [
    path("register/", RegistrateView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(
        template_name='account/login.html',
        next_page=reverse_lazy('core:home'),
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # change passwd
    path('password-change/', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy("account:password_change_done"),
        template_name='account/password-change.html'
    ), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password-change-done.html'
    ), name='password_change_done'),

    # reset passwd
    path('reset-passwd/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy("account:password_reset_done"),
        template_name='account/password_reset.html',
        email_template_name='account/password_reset_email.html',
        form_class=MyPasswordResetForm
    ), name='password_reset'),
    path('reset-passwd-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset-passwd-confirm/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html',
        success_url = reverse_lazy("account:password_reset_complete")
    ),
         name='password_reset_confirm'),
    path('reset-passwd-complate/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'
    ), name='password_reset_complete'),

]
