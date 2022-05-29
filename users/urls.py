from unicodedata import name
from django.urls import path
from . import views



# define namespace for the app

urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('userhome',views.user_home,name='userhome'),



    #####
    path('adminCharts', views.AdminCharts.as_view(),name='admin-charts'),
    path('adminhome',views.admin_home,name='adminhome'),
    path('adminProfile',views.admin_profile,name='adminProfile'),
    path('adminProfile/edit',views.admin_profile_edit,name='editAdminProfile'),
    #####
]