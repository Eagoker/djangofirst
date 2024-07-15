from django import forms
from .models import *


class StarForm(forms.ModelForm):
    class Meta:
        model = Stars
        fields = ["name", "surname", "age", "condition", "profession"]