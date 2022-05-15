from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.userHome, name='home'),
    path('login', views.login, name='login'),
]

