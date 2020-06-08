"""
Urls
"""
from django.urls import include, path
from rest_framework import routers
from mainApp import views
from . import views

router = routers.DefaultRouter()
router.register(r'minor', views.MinorSet)
router.register(r'waypoint', views.WaypointSet)

urlpatterns = [
    path('api/minor-waypoint-history', views.MinorWaypointHistoryView.as_view()),
    path('api/', include(router.urls)),
]
