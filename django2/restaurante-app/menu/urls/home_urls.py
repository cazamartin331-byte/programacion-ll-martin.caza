from django.urls import path

from menu.views.home_views import home

urlpatterns = [
    path('', home, name='home'),
]
