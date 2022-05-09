import imp
from django.db import models
from products.models import Product

# Create your models here.

class Seller (models.Model):
    companyName=models.CharField(max_length=25, null=False)
    taxNumber=models.CharField(max_length=25, null=False)
    sellerEmail=models.EmailField(primary_key=True,null=False)
    sellerPassword=models.CharField(max_length=20, null=False)
    companyDiscription=models.TextField(default="no discription available", null=True)
    sellerPhoto=models.ImageField('photos/%y/%m/%d', null=True, default='media/profilePic.jpg') #check media, put defalt photo
    sellerProducts=models.ForeignKey(Product,on_delete=models.CASCADE)
    signedIn=models.BooleanField(default=False)

    
