from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "w-full p-2 border rounded"}),
            "email": forms.EmailInput(attrs={"class": "w-full p-2 border rounded"}),
            "password1": forms.PasswordInput(attrs={"class": "w-full p-2 border rounded"}),
            "password2": forms.PasswordInput(attrs={"class": "w-full p-2 border rounded"}),
        }

    username = forms.CharField(label="Nom d'utilisateur")
    email = forms.EmailField(label="Adresse e-mail")
    password1 = forms.CharField(label="Mot de passe")
    password2 = forms.CharField(label="Confirmer le mot de passe")


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(
        attrs={"class": "w-full p-2 border rounded"}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
        attrs={"class": "w-full p-2 border rounded"}))
