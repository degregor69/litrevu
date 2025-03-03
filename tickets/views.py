from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TicketForm
from .models import Ticket


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associer le ticket à l'utilisateur connecté
            ticket.save()
            return redirect("signin_success")  # À remplacer par la page où l'on veut rediriger
    else:
        form = TicketForm()

    return render(request, "tickets/create_ticket.html", {"form": form})

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by("-time_created")
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})


@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.user != request.user:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à modifier ce ticket.")
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("ticket_list")
    else:
        form = TicketForm(instance=ticket)

    return render(request, "tickets/update_ticket.html", {"form": form, "ticket": ticket})