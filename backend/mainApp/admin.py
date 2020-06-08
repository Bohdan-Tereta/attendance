"""
Admin pages
"""
from django.contrib import admin
from.models import Device, Minor, MinorWaypointHistory, Waypoint

# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """
    Admin pages for Devices
    """
    readonly_fields = ('id', 'created_at', 'updated_at', 'creator', 'updater')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.creator = request.user
        obj.updater = request.user
        super().save_model(request, obj, form, change)
    list_display = ('id', 'code', 'device_type', 'description')

@admin.register(Minor)
class MinorAdmin(admin.ModelAdmin):
    """
    Admin pages for Minors
    """
    list_display = ('id', 'user_id', 'current_grade')

@admin.register(MinorWaypointHistory)
class MinorWaypointHistoryAdmin(admin.ModelAdmin):
    """
    Admin pages for MinorWaypoints
    """
    list_display = ('id', 'minor_id', 'waypoint_id', 'created_at')

@admin.register(Waypoint)
class WaypointAdmin(admin.ModelAdmin):
    """
    Admin pages for Waypoints
    """
    readonly_fields = ('id', 'created_at', 'updated_at', 'creator', 'updater')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.creator = request.user
        obj.updater = request.user
        super().save_model(request, obj, form, change)
    list_display = ('id', 'code', 'address', 'device_id', 'description')
