from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from reviews.models import Review
from tickets.models import Ticket
from .forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return signup_success(request)
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "users/login.html"

    success_url = reverse_lazy("signin_success")

    def get_success_url(self):
        return self.success_url

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("login"))


def signup_success(request):
    return render(request, "users/signup_success.html")

def signin_success(request):
    return render(request, "users/signin_success.html")

def user_posts(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    user_reviews = Review.objects.filter(user=request.user)

    context = {
        "user_tickets": user_tickets,
        "user_reviews": user_reviews
    }

    return render(request, "users/posts.html", context)