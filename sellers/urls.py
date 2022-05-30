from django.urls import path
from . import views

# define namespace for the app

urlpatterns = [
    path('signupBusiness', views.signupBusiness, name='signupBusiness'),
    path('sellerhome',views.seller_home,name='sellerhome'),
    path('ajax-validation', views.ajax,name='signup_validation'),
]