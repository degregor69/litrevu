from itertools import chain

from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value

from follows.models import UserFollows
from reviews.models import Review
from .forms import TicketForm
from .models import Ticket


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("signin_success")
    else:
        form = TicketForm()

    return render(request, "tickets/create_ticket.html", {"form": form})

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

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if ticket.user != request.user:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à supprimer ce ticket.")

    if request.method == "POST":
        ticket.delete()
    return redirect("ticket_list")


@login_required
def feed(request):
    user = request.user
    followed_users = UserFollows.objects.filter(user=user).values_list('followed_user', flat=True)

    tickets = Ticket.objects.filter(user__in=list(followed_users) + [user]).annotate(
        content_type=Value('TICKET', CharField()))

    user_tickets = Ticket.objects.filter(user=user)
    reviews = Review.objects.filter(ticket__in=user_tickets) | Review.objects.filter(
        user__in=list(followed_users) + [user])
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    return render(request, 'tickets/feed.html', {'posts': posts})