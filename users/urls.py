from django.urls import path
from .views import signup_view, login_view, signup_success, signin_success, logout_view, user_posts

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup-success/", signup_success, name="signup_success"),
    path("signin-success/", signin_success, name="signin_success"),
    path("posts/", user_posts, name="posts"),

]
