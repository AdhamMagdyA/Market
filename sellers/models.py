from django.db import models
from django.db import models
from datetime import datetime
from core.models import Authorization

# Create your models here.
DEFAULT_CASE_ID=1
class Seller (models.Model):
    user_id = models.AutoField(primary_key=True,)
    companyName=models.CharField(max_length=25, null=False)
    taxNumber=models.CharField(max_length=25, null=False)
    email=models.EmailField(null=False)
    password=models.CharField(max_length=20, null=False)
    companyDiscription=models.TextField(default="no discription available", null=True)
    sellerPhoto=models.ImageField(upload_to = 'photos/%y/%m/%d', null=True, default='media/profilePic.jpg') #check media, put defalt photo
    
    # changed the relationship implementation to make the product carry the seller info
    # sellerProducts=models.ForeignKey(Product,on_delete=models.CASCADE)

    is_active=models.BooleanField(default=True)
    last_login=models.DateField(default= datetime.now)
    userAuth=models.ForeignKey(Authorization,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.companyName

    
    def check_password(self,password,**kwargs):
        if self.password==password :
            print('in check_password for seller')
            return True
        else :
            return False
    

    
