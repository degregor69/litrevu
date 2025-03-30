from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.TextField(
        max_length=2048, blank=True, verbose_name="Description")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    image = models.ImageField(null=True, blank=True,
                              upload_to="tickets_images/", verbose_name="Image")
    time_created = models.DateTimeField(auto_now_add=True)

    def has_user_review(self, user):
        return self.review_set.filter(user=user).exists()
