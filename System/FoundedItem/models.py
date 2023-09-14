from django.db import models

# Create your models here.
   
    
class founded_items_details(models.Model):
    name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    founded_date = models.DateField()
    founded_time = models.TimeField()
    location = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    additional_comments = models.TextField(blank=True,default="---")
    # photo = models.FileField(upload_to="lost_items/",max_length=250,null=True,default=None,blank=True)
    photo = models.ImageField(upload_to="founded_items/",blank=True,null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name:- {self.name} ----- Contact Name:- {self.contact_name} ----- Mob Number:- {self.phone_number}  ----- Photo:- {self.photo}"