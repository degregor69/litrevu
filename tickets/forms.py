from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full p-2 border rounded"}),
            "description": forms.Textarea(attrs={"class": "w-full p-2 border rounded", "rows": 4}),
            "image": forms.ClearableFileInput(attrs={"class": "w-full p-2 border rounded"}),
        }
