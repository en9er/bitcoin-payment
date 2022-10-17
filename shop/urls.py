from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_card, name='create'),
    path('view/card/<str:slug>/', views.CardDetailView.as_view(), name='product_detail')
]