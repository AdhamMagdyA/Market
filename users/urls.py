from django.urls import path
from . import views

# define namespace for the app

urlpatterns = [
    path('signupBusiness', views.signupBusiness, name='signupBusiness'),
    path('signup', views.signup,name='signup'),
    path('login', views.login, name='login'),

]