from django.contrib import admin
from .models import Bike,Car,Other,Reports

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['ID','Title','Image','Date']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['ID','Title','Image','Date']

@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = ['ID','Title','Image','Date']

@admin.register(Reports)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['ID','Issue']