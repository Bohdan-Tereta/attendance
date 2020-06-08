from django.shortcuts import render
from django.http import HttpResponse
from .models import Minor, MinorWaypointHistory, Waypoint
from rest_framework import viewsets
from .serializers import MinorSerializer, MinorWaypointHistorySerializer



# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MinorWaypointHistorySet(viewsets.ModelViewSet):
    """
    API endpoint that allows MinorWaypointHistory to be viewed
    """
    queryset = MinorWaypointHistory.objects.all().order_by('-created_at')
    serializer_class = MinorWaypointHistorySerializer

class MinorSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MinorWaypointHistory to be viewed
    """
    queryset = Minor.objects.all().order_by('-created_at')
    serializer_class = MinorSerializer

class WaypointSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MinorWaypointHistory to be viewed
    """
    queryset = Waypoint.objects.all().order_by('-created_at')
    serializer_class = MinorSerializer
