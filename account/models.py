from django.contrib.auth.models import AbstractUser
from django.db import models
from wallet.models import Wallet
from django.dispatch import receiver
from django.db.models.signals import post_delete


class CustomUser(AbstractUser):
    has_wallet = models.BooleanField(default=False)
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE, null=True)
    # if your additional field is a required field, just add it, don't forget to add 'email' field too.
    REQUIRED_FIELDS = ['has_wallet', 'email']
