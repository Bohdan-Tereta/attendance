"""
Views
"""
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MinorWaypointHistory
from .serializers import MinorWaypointHistorySerializer



# Create your views here.

class MinorWaypointHistoryView(APIView):
    """
    API endpoint that allows MinorWaypointHistory to be viewed
    """
    def get(self, request):
        """
        Get current waypoints for each minor
        """
        queryset = MinorWaypointHistory.objects.raw('''
SELECT p1.id
FROM mainapp_minorwaypointhistory p1, (
    SELECT minor_id_id, MAX(created_at) AS max_created_at
    FROM mainapp_minorwaypointhistory
    GROUP BY minor_id_id
) AS p2
WHERE p1.minor_id_id = p2.minor_id_id AND p1.created_at = p2.max_created_at
''')
        serializer = MinorWaypointHistorySerializer(queryset, many=True)
        return Response(serializer.data)
        