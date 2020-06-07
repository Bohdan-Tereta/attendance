from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
    code = models.CharField(max_length=50)
    description  = models.CharField(max_length=50)
    device_type  = models.CharField(max_length=50)  
    disabled = models.BooleanField()
    #creator = models.ForeignKey(User,on_delete=models.CASCADE,)
    #updater = LastUserField(on_delete=models.CASCADE,) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)