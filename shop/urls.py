from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_product, name='add_product'),
    path('view/card/<str:slug>/', views.CardDetailView.as_view(), name='product_detail')
]