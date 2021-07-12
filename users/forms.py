from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    """Customized form that creates users"""

    email = forms.EmailField(max_length=255, help_text="Obligatoire")
    username = forms.CharField(max_length=60, help_text="Obligatoire")

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


class UserAuthenticationForm(UserCreationForm):
    """Customized form that authenticate users"""
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password2']
