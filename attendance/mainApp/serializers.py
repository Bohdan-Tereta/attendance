from .models import Minor, MinorWaypointHistory, Waypoint
from rest_framework import serializers

class MinorWaypointHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinorWaypointHistory
        fields = ['id', 'minor_id', 'waypoint_id', 'created_at']

class MinorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Minor
        fields = ['id']

class WaypointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['id']