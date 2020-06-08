"""
Urls
"""
from django.urls import include, path
from rest_framework import routers
from mainApp import views
from . import views

router = routers.DefaultRouter()
router.register(r'minor-waypoint-history', views.MinorWaypointHistorySet)
router.register(r'minor', views.MinorSet)
router.register(r'waypoint', views.WaypointSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
