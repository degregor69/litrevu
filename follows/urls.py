from django.urls import path
from .views import follows_index, unfollow, follow

urlpatterns = [
    path('', follows_index, name='follows_index'),
    path("unfollow/<int:follow_id>/", unfollow, name="unfollow"),
    path('follow/', follow, name='follow'),
]
