from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from tickets.models import Ticket
from .forms import TicketReviewForm, ReviewForm
from .models import Review


@login_required
def create_ticket_review(request):
    if request.method == "POST":
        form = TicketReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("ticket_list")
    else:
        form = TicketReviewForm()

    return render(request, "reviews/create_ticket_review.html", {"form": form})

@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if Review.objects.filter(ticket=ticket, user=request.user).exists():
        return redirect("ticket_list")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("ticket_list")
    else:
        form = ReviewForm()
    return render(request, "reviews/create_review.html", {"form": form, "ticket": ticket})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return redirect("ticket_list")

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("ticket_list")
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/edit_review.html", {"form": form})