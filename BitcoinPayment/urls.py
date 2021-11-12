from django.contrib import admin
from django.urls import path, include
from BitcoinPayment import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('shop.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls)
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR)