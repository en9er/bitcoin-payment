from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="wallet"),
    path('create', views.create_wallet, name="create_wallet"),
]