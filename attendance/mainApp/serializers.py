"""
Serializers
"""
from rest_framework import serializers
from .models import Minor, MinorWaypointHistory, Waypoint

class MinorWaypointHistorySerializer(serializers.HyperlinkedModelSerializer):
    """
    MinorWaypointHistory serializer
    """
    class Meta:
        model = MinorWaypointHistory
        fields = ['id', 'minor_id', 'waypoint_id', 'created_at']

class MinorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Minor serializer
    """
    class Meta:
        model = Minor
        fields = ['id']

class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    """
    Waypoint serializer
    """
    class Meta:
        model = Waypoint
        fields = ['id']
