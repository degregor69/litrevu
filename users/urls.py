from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup_view, CustomLoginView, signup_success, signin_success

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup-success/", signup_success, name="signup_success"),
    path("signin-success/", signin_success, name="signin_success"),
]
