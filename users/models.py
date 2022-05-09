from asyncio.windows_events import NULL
from django.db import models
from carts.models import Cart

# Create your models here.

class User (models.Model):
    userFirstName=models.CharField(max_length=25, default=NULL,blank=False, null=False)
    userLastName=models.CharField(max_length=25, default=NULL,blank=False, null=False)
    userEmail=models.EmailField(primary_key=True, null=False)
    userPassword=models.CharField(max_length=20, null=False)
    userPhoto=models.ImageField('photos/%y/%m/%d', null=True, default='media/profilePic.jpg') #check media, put defalt photo
    userCart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    preferedUserCategories=[] #preferedUserCategories.append(frontendvalue)
    signedIn=models.BooleanField(default=False)

    class privilageType(models.TextChoices):
        ADMIN = 'AD'
        USER = 'US'
        SELLER='SE'
        

    userType = models.CharField(max_length=2, choices=privilageType.choices,default=privilageType.USER )
    #we assign this field as userType = 'US' in the front

    def __str__(self):
        return self.userName
    class Meta:
        verbose_name='NormalUsers'
        ordering = ['userFirstName']
    



        
        

    
    
