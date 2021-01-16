from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('products', include('products.urls')),
    path('', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
]
