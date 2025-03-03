from django.urls import path
from .views import create_ticket_review

urlpatterns = [
    path("create/", create_ticket_review, name="create_ticket_review"),
]
