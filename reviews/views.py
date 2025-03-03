from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TicketReviewForm

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
