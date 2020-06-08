"""
Urls
"""
from django.urls import path
from mainApp import views
from . import views


urlpatterns = [
    path('api/minor-waypoint-history', views.MinorWaypointHistoryView.as_view()),
]
