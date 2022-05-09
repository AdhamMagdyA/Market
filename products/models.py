from datetime import datetime
from django.db import models
#####from users.models import User


# Create your models here.

class Product(models.Model):
    productName =models.CharField(max_length=20,blank=True, null=True)
    productDiscription=models.TextField(default='no discription', null=True)
    productImage=models.ImageField(upload_to=('photos/%y/%m/%d'),default='media/productPic.jpg', null=True) #check media, put defalt photo
    uploadingDate=models.DateField(default= datetime.now)
    productPrice=models.DecimalField(max_digits=8, decimal_places=2)
    productActivation=models.BooleanField(default=False)




    #####productDiscription=models.TextField(choices=User.Categories.choices,)
    class Categories(models.TextChoices):
        NONE = 'NONE'
        HOMEELECTRONICS = 'HOMEELECTRONICS'
        PHONE = 'USER'
        LAPTOPS='SELLER'
        WOMENWEAR='WOMENWEAR'
        MENWEAR='MENWEAR'
        KIDSWEAR='KIDSEWAR'
        FURNATURE='FURNATURE'
        GAMES='GAMES'

        #...........................
        #and if there is a slight chance that choices could be dynamically added or removed, 
        #they are not the right path to choose. I hope this article helped you!
    
    productDiscription=models.TextField(choices=Categories.choices,null=False, default=Categories.NONE) #productDiscription = value



    def __str__(self):
        return self.productName
    class Meta:
        verbose_name='products'
        ordering = ['uploadingDate']
