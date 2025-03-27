from django.urls import path
from .views import create_ticket, update_ticket, delete_ticket, feed

urlpatterns = [
    path("create/", create_ticket, name="create_ticket"),
    path("edit/<int:ticket_id>/", update_ticket, name="update_ticket"),
    path("delete/<int:ticket_id>/", delete_ticket, name="delete_ticket"),
    path('feed/', feed, name='feed'),
    path('', feed, name='feed')
]
