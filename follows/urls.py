from django.urls import path
from .views import follows_index, unfollow

urlpatterns = [
    path('', follows_index, name='following_list'),
    path('unfollow/<int:follow_id>/', unfollow , name='unfollow')
]
