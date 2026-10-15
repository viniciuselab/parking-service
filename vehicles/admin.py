from django.contrib import admin
from .models import Vehicle, VehiclesType

# Register your models here.

@admin.register(VehiclesType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color']
    search_fields = ['license_plate', 'model']
    list_filter = ['vehicle_type']