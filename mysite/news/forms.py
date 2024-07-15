from .models import News
from django import forms
import re
from django.core.exceptions import ValidationError


class NewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Название не должно начинаться с цифры!")
        return title

    def clean_is_published(self):
        is_published = self.cleaned_data['is_published']
        if is_published is False:
            raise ValidationError("Не заполнено!")
        return is_published