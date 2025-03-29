"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from litrevu import settings
from users.views import user_posts
from tickets.views import feed
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", feed, name="feed"),
    path("users/", include("users.urls")),
    path("tickets/", include("tickets.urls")),
    path("reviews/", include("reviews.urls")),
    path("follows/", include("follows.urls")),
    path("posts/", user_posts, name="posts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
