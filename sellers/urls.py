from django.urls import path
from . import views

# define namespace for the app

urlpatterns = [
    path('signupBusiness', views.signupBusiness, name='signupBusiness'),
    path('sellerhome',views.seller_home,name='sellerhome'),
]