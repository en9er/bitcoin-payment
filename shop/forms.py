from django import forms

from .models import Card


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['image', 'title', 'description']
