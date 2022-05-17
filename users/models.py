from asyncio.windows_events import NULL
from django.db import models
from carts.models import Cart
from products.models import Category
from core.models import Authorization
from datetime import datetime
# Create your models here.

  

DefaultPreCat=1
DEFAULT_CASE_ID=2
class User (models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=25, default=NULL, null=False)
    last_name=models.CharField(max_length=25, default=NULL, null=False)
    email=models.EmailField(unique=True, null=False)
    password=models.CharField(max_length=20, null=False)
    userPhoto=models.ImageField(upload_to = 'photos/%y/%m/%d', null=True, default='media/profilePic.jpg') #check media, put defalt photo
    userCart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    last_login=models.DateField(default= datetime.now)
    is_active=models.BooleanField(default=True)
    userAuth=models.ForeignKey(Authorization,on_delete=models.PROTECT,null=True)

    
    # preferedUserCategories=models.ForeignKey(Category, on_delete=models.PROTECT, default=DefaultPreCat)
    



    
    #we assign this field as userType = 'US' in the front





    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name='NormalUsers'
        ordering = ['first_name']



    def check_password(self,password,**kwargs):
        if self.password==password :
            return True
        else :
            return False
    



    

    
    






















# preferedUserCategories=[] #preferedUserCategories.append(frontendvalue)



# class privilageType(models.TextChoices):
#         ADMIN = 'AD'
#         USER = 'US'
#         SELLER='SE'
        

#     userType = models.CharField(max_length=2, choices=privilageType.choices,default=privilageType.USER )