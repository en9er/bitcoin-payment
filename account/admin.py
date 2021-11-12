from django.contrib import admin
from wallet.models import Wallet
from account.models import CustomUser

admin.site.register(Wallet)
admin.site.register(CustomUser)
