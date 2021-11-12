from django.db import models


class Wallet(models.Model):
    is_activated = models.BooleanField(default=False)
    address = models.CharField(max_length=256, unique=True)
    public_key = models.CharField(max_length=256)
    addiction_info = models.CharField(max_length=256, default="", null=True)

    def __str__(self):
        return self.address