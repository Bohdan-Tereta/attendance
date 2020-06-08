"""
Models
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
    """
    Device model
    """
    code = models.CharField(
        max_length=50,
        unique=True,
        )
    description = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)
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
    def __str__(self):
        return self.code

class Waypoint(models.Model):
    """
    Waypoint model
    """
    device_id = models.OneToOneField(
        Device,
        models.CASCADE
    )
    code = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
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
    def __str__(self):
        return self.description

class Minor(models.Model):
    """
    Minor model
    """
    user_id = models.ForeignKey(
        User,
        models.CASCADE
    )
    current_grade = models.PositiveSmallIntegerField()
    def __str__(self):
        return User.objects.filter(id=self.user_id.id).first().username

class MinorWaypointHistory(models.Model):
    """
    MinorWaypointHistory model
    """
    minor_id = models.ForeignKey(
        Minor,
        models.CASCADE
    )
    waypoint_id = models.ForeignKey(
        Waypoint,
        models.CASCADE
    )
    created_at = models.DateTimeField()
