from unicodedata import name
from django.urls import path
from . import views

# define namespace for the app

urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('userhome',views.user_home,name='userhome'),



    #####
    path('adminhome',views.admin_home,name='adminhome')
]