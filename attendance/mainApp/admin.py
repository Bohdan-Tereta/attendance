from django.contrib import admin
from.models import Device, Waypoint

# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at','creator', 'updater')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.creator = request.user
        obj.updater = request.user
        super().save_model(request, obj, form, change)

@admin.site.register(Waypoint)