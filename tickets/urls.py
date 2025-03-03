from django.urls import path
from .views import create_ticket, ticket_list, update_ticket, delete_ticket

urlpatterns = [
    path("create/", create_ticket, name="create_ticket"),
    path("", ticket_list, name="ticket_list"),
    path("edit/<int:ticket_id>/", update_ticket, name="update_ticket"),
    path("delete/<int:ticket_id>/", delete_ticket, name="delete_ticket")
]
