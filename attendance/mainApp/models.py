from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
    code = models.CharField(max_length=50)
    description  = models.CharField(max_length=50)
    device_type  = models.CharField(max_length=50)  
    disabled = models.BooleanField()
    creator = models.ForeignKey(
        User,
        models.CASCADE,
        'device_to_user_created'
    )
    updater = models.ForeignKey(
        User,
        models.CASCADE,
        'device_to_user_added'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Waypoint(models.Model):
    device_id = models.ForeignKey(
        Device,
        models.CASCADE
    )
    code = models.CharField(max_length=50)
    description  = models.CharField(max_length=50)
    address  = models.CharField(max_length=50)
    disabled = models.BooleanField()
    creator = models.ForeignKey(
        User,
        models.CASCADE,
        'waypoint_to_user_created'
    )
    updater = models.ForeignKey(
        User,
        models.CASCADE,
        'waypoint_to_user_added'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)