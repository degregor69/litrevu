from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TicketForm


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
