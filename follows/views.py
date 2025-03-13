from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserFollows
from users.models import CustomUser

@login_required
def follows_index(request):
    all_users = CustomUser.objects.exclude(id=request.user.id).filter(is_superuser=False)
    followers = UserFollows.objects.filter(followed_user=request.user)
    following = UserFollows.objects.filter(user=request.user)

    following_ids = following.values_list("followed_user__id", flat=True)
    users_to_follow = all_users.exclude(id__in=following_ids)
    return render(request, "follows_index.html", {"users_to_follow": users_to_follow,"followers": followers, "following": following})

@login_required
def unfollow(request, follow_id):
    follow = get_object_or_404(UserFollows, id=follow_id, user=request.user)
    follow.delete()
    return redirect("follows_index")


@login_required
def follow(request):
    user_id = request.POST.get('user_id')
    if user_id:
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if not UserFollows.objects.filter(user=request.user, followed_user=user_to_follow).exists():
            UserFollows.objects.create(user=request.user, followed_user=user_to_follow)

    return redirect('follows_index')
