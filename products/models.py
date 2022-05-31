from cgitb import small
from datetime import datetime
from django.db import models

from sellers.models import Seller
#####from users.models import User


# Create your models here.


class Category (models.Model):
    categoryName =models.CharField(max_length=25)

    def __str__(self):
        return self.categoryName

_now = datetime.now()
year=_now.strftime('%Y')
month=_now.strftime('%m')
day=_now.strftime('%d')

DEFAULT_CASE=1
class Product(models.Model):
    productName =models.CharField(max_length=20,blank=True, null=True)
    productDiscription=models.TextField(default='no discription', null=True)
    productImage=models.ImageField(upload_to=('photos/%y/%m/%d'),default='productPic.jpg', null=True) #check media, put defalt photo
    uploadingDate=models.DateField(default= datetime.now)
    productPrice=models.DecimalField(max_digits=8, decimal_places=2)
    productOldPrice=models.DecimalField(max_digits=8, decimal_places=2, null=True)
    # when the login is done we should change the null to false
    productSeller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    available=models.DecimalField(max_digits=8,decimal_places=0)
    sold=models.DecimalField(max_digits=8, decimal_places=0)
    # calculate discount from productOldPrice and productPrice
    def discount(self):
        if self.productOldPrice:
            return int(round(((self.productOldPrice-self.productPrice)/self.productOldPrice)*100,2))
        else:
            return 0
    productActivation=models.BooleanField(default=False)
    category=models.ForeignKey(Category, on_delete=models.PROTECT,default=DEFAULT_CASE)
    def __str__(self):
        return self.productName
    class Meta:
        verbose_name='products'
        ordering = ['uploadingDate']










    











    # #####productDiscription=models.TextField(choices=User.Categories.choices,)
    # class Categories(models.TextChoices):
    #     NONE = 'NONE'
    #     HOMEELECTRONICS = 'HOMEELECTRONICS'
    #     PHONE = 'USER'
    #     LAPTOPS='SELLER'
    #     WOMENWEAR='WOMENWEAR'
    #     MENWEAR='MENWEAR'
    #     KIDSWEAR='KIDSEWAR'
    #     FURNATURE='FURNATURE'
    #     GAMES='GAMES'

    #     #...........................
    #     #and if there is a slight chance that choices could be dynamically added or removed, 
    #     #they are not the right path to choose. I hope this article helped you!
    
    # productDiscription=models.TextField(choices=Categories.choices,null=False, default=Categories.NONE) #productDiscription = value

