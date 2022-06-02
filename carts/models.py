from asyncio.windows_events import NULL
from unicodedata import name
from django.db import models
from products.models import Product

# Create your models here.

class Cart(models.Model):
    
    cartName=models.CharField(max_length=30, default="My Cart")
    cartProducts=models.ManyToManyField(Product)

    def __str__(self):
        return self.cartName

