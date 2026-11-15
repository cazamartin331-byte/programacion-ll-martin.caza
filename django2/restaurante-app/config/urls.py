from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('menu.urls.authentication_urls')),
    path('', include('menu.urls')),
]
