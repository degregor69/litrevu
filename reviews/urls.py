from django.urls import path
from .views import create_ticket_review, create_review, edit_review, delete_review

urlpatterns = [
    path(
        "create/",
        create_ticket_review,
        name="create_ticket_review"),
    path(
        "review/edit/<int:review_id>/",
        edit_review,
        name="edit_review"),
    path(
        "review/create/<int:ticket_id>/",
        create_review,
        name="create_review"),
    path(
        'reviews/delete/<int:review_id>/',
        delete_review,
        name='delete_review'),
]
