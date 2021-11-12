from django import forms
from .models import CustomUser
from wallet.models import Wallet
from wallet import HDwallet
from django.contrib.auth.forms import UserCreationForm


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=256, label="Username")
    password = forms.CharField(max_length=256, label="Password", widget=forms.PasswordInput)
    fields = ('username', 'password')
