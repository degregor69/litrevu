from django.urls import path
from .views import signup_view, CustomLoginView, signup_success, signin_success, logout_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup-success/", signup_success, name="signup_success"),
    path("signin-success/", signin_success, name="signin_success"),

]
