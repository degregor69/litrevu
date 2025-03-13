from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserFollows

@login_required
def follows_index(request):
    followers = UserFollows.objects.filter(followed_user=request.user)  # Ceux qui suivent l'utilisateur
    following = UserFollows.objects.filter(user=request.user)  # Ceux que l'utilisateur suit

    return render(request, "follows_index.html", {"followers": followers, "following": following})

@login_required
def unfollow(request, follow_id):
    follow = get_object_or_404(UserFollows, id=follow_id, user=request.user)
    follow.delete()
    return redirect("follows_index.html")