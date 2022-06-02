from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.userHome, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.userProfile, name='profile'),
    path('profile/edit', views.userEditProfile, name='edit_profile'),
]

