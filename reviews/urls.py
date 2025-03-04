from django.urls import path
from .views import create_ticket_review, edit_review

urlpatterns = [
    path("create/", create_ticket_review, name="create_ticket_review"),
    path("review/edit/<int:review_id>/", edit_review, name="edit_review"),
]
