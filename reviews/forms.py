from django import forms
from tickets.models import Ticket
from tickets.views import ticket_list
from .models import Review


class TicketReviewForm(forms.ModelForm):
    headline = forms.CharField(label="Titre de la critique", max_length=128, required=True)
    rating = forms.IntegerField(label="Note (0-5)", min_value=0, max_value=5, required=True)
    body = forms.CharField(label="Votre critique", widget=forms.Textarea, required=True)

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]

    def save(self, user):
        ticket = Ticket.objects.create(
            user=user,
            title=self.cleaned_data["title"],
            description=self.cleaned_data["description"],
            image=self.cleaned_data["image"]
        )

        review = Review.objects.create(
            user=user,
            ticket=ticket,
            headline=self.cleaned_data["headline"],
            rating=self.cleaned_data["rating"],
            body=self.cleaned_data["body"]
        )

        return ticket_list
