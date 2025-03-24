from django.urls import path
from .views import follows_index, unfollow, follow, search_users

urlpatterns = [
    path('', follows_index, name='follows_index'),
    path("unfollow/<int:follow_id>/", unfollow, name="unfollow"),
    path('follow/', follow, name='follow'),
    path("search-users/", search_users, name="search_users"),
]
