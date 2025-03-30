from django import forms
from tickets.models import Ticket
from tickets.views import feed
from .models import Review


class TicketReviewForm(forms.ModelForm):
    headline = forms.CharField(
        label="Titre de la critique",
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={"class": "w-full p-2 border rounded"})
    )
    rating = forms.IntegerField(
        label="Note (0-5)",
        min_value=0,
        max_value=5,
        required=True,
        widget=forms.NumberInput(
            attrs={"class": "w-full p-2 border rounded", "min": 0, "max": 5})
    )
    body = forms.CharField(
        label="Votre critique",
        required=True,
        widget=forms.Textarea(
            attrs={"class": "w-full p-2 border rounded", "rows": 4})
    )

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full p-2 border rounded"}),
            "description": forms.Textarea(attrs={"class": "w-full p-2 border rounded", "rows": 4}),
            "image": forms.ClearableFileInput(attrs={"class": "w-full p-2 border rounded"}),
        }

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

        return feed


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]

        widgets = {
            "headline": forms.TextInput(attrs={"class": "w-full p-2 border rounded"}),
            "rating": forms.NumberInput(attrs={"class": "w-full p-2 border rounded", "min": 0, "max": 5}),
            "body": forms.Textarea(attrs={"class": "w-full p-2 border rounded", "rows": 4}),
        }
