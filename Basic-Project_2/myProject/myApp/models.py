from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):

    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    ]
    
    USER=[
        ('viewers','Viewers'),
        ('blogers','Blogers'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Gender=models.CharField(max_length=100,null=True,choices=GENDER)
    Age=models.PositiveIntegerField(null=True)
    Contact_No=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to="Media/profile_pic",null=True)
    
    
    def __str__(self):  
        
        return f"{self.username}-{self.Age}"
    
class viewersProfileModel(models.Model):
    
    PREFERRD_CONTENT=[
        ('articlse','Articlse'),
        ('videos','Videos'),
        ('both','Both'),
    ]
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='viewersProfile')
    Bio=models.TextField(max_length=100,null=True)
    interested=models.CharField(max_length=100,null=True)
    preferred_content_type=models.CharField(max_length=100,null=True,choices=PREFERRD_CONTENT)
    locations=models.CharField(max_length=100,null=True)
    def __str__(self):
        return f"{self.user.username}"
    
    
class bologerProfileModel(models.Model):
    
   
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='bologerProfile')
    Bio=models.TextField(max_length=100,null=True)
    website_url=models.URLField(blank=True,null=True)
    locations=models.CharField(max_length=100,null=True)

   
    def __str__(self):
        return f"{self.user.username}"
    




    
  