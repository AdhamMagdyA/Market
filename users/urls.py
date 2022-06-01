from unicodedata import name
from django.urls import path
from . import views



# define namespace for the app

urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('ajax-validation', views.ajax,name='signup_validation'),
    path('userhome',views.user_home,name='userhome'),



    #####
    path('adminCharts', views.AdminCharts.as_view(),name='admin-charts'),
    path('adminhome',views.admin_home,name='adminhome'),
    path('listusers',views.admin_list_user,name='list_users'),
    path('sus-adm-fet',views.sus_adm_fet,name='sus-adm-fet'),
    path('listproducts',views.admin_list_product,name='list_products'),
    path('adminProfile',views.admin_profile,name='adminProfile'),
    path('adminProfile/edit',views.admin_profile_edit,name='editAdminProfile'),
    #####
]