from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from BitcoinPayment import settings
urlpatterns = [
    path('', views.account, name='account'),
    path('register', views.register, name='account_register'),
    path('wallet/', include('wallet.urls')),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
]
