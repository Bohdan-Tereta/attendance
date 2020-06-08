"""
Serializers
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Minor, MinorWaypointHistory, Waypoint

class MinorWaypointHistorySerializer(serializers.ModelSerializer):
    """
    MinorWaypointHistory serializer for GET
    """
    class MinorSerializer(serializers.ModelSerializer):
        """
        Minor userName, firstName, lastName, grade serializer
        """
        class UserSerializer(serializers.ModelSerializer):
            """
            User userName, firstName, lastName serializer
            """
            class Meta:
                model = User
                fields = ['id', 'username', 'first_name', 'last_name']
        user_id = UserSerializer()
        class Meta:
            model = Minor
            fields = ['id', 'current_grade', 'user_id']
    class WaypointSerializer(serializers.ModelSerializer):
        """
        Waypoint address and description serializer
        """
        class Meta:
            model = Waypoint
            fields = ['id', 'address', 'description']
    minor_id = MinorSerializer()
    waypoint_id = WaypointSerializer()
    class Meta:
        model = MinorWaypointHistory
        fields = ['id', 'minor_id', 'waypoint_id', 'created_at']

class MinorWaypointHistoryPostSerializer(serializers.ModelSerializer):
    """
    MinorWaypointHistory serializer for POST
    """
    class Meta:
        model = MinorWaypointHistory
        fields = ['id', 'minor_id', 'waypoint_id', 'created_at']
        