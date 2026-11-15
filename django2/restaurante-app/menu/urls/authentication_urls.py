from django.urls import path

from menu.views.authentication_views import MenuLoginView, MenuLogoutView

urlpatterns = [
    path('login/', MenuLoginView.as_view(), name='login'),
    path('logout/', MenuLogoutView.as_view(), name='logout'),
]
