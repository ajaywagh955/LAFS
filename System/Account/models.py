from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class User_Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    auth_token = models.CharField(max_length=100,default="")
    is_varified = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return f"User:- {self.user} ----- Full Name:- {self.full_name} ----- Mobile Number:- {self.mobile_number}"
    