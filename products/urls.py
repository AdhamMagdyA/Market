from django.urls import path, include
from . import views

# define namespace for the app
app_name = 'products'

urlpatterns = [
    path('', views.index, name='products'),
    path('add', views.add, name='add'),
    path('get/<int:id>', views.get, name='get'),
]