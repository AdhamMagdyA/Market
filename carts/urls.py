from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='cart'),
    path('<int:id>',views.addToCart, name='addToCart1'),
    path('remove/<int:id>',views.removeFromCart, name='removeFromCart'),
]