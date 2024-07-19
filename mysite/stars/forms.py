from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StarForm(forms.ModelForm):
    class Meta:
        model = Stars
        fields = ("name", "surname", "age", "condition", "profession")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
