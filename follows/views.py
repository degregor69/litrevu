from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import UserFollows
from users.models import CustomUser


@login_required
def follows_index(request):
    followers = UserFollows.objects.filter(followed_user=request.user)
    following = UserFollows.objects.filter(user=request.user)

    following_ids = following.values_list("followed_user__id", flat=True)

    all_users = CustomUser.objects.exclude(
        id=request.user.id).filter(is_superuser=False)
    users_to_follow = all_users.exclude(id__in=following_ids)
    return render(request, "follows_index.html", {"users_to_follow": users_to_follow, "followers": followers, "following": following})


@login_required
def unfollow(request, follow_id):
    follow = get_object_or_404(UserFollows, id=follow_id, user=request.user)
    follow.delete()
    return redirect("follows_index")


@login_required
def follow(request):
    message = None
    if request.method == "POST":
        username = request.POST.get("username")

        if not username:
            message = "Veuillez entrer un nom d'utilisateur."
        else:
            user_to_follow = CustomUser.objects.filter(
                username=username).first()

            if not user_to_follow:
                message = f"L'utilisateur '{username}' n'existe pas."
            elif UserFollows.objects.filter(user=request.user, followed_user=user_to_follow).exists():
                message = f"Vous suivez déjà {user_to_follow.username}."
            else:
                UserFollows.objects.create(
                    user=request.user, followed_user=user_to_follow)
                message = f"Vous suivez maintenant {user_to_follow.username} !"

    return render(request, "follows_index.html", {
        "following": UserFollows.objects.filter(user=request.user),
        "followers": UserFollows.objects.filter(followed_user=request.user),
        "message": message,
    })
