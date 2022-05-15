from typing import Tuple
from django.db import models

# Create your models here.

class Authorization(models.Model):
    auth_name = models.CharField(max_length=50,default='None')

    def __str__(self) :
        return self.auth_name

