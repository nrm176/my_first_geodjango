from django.contrib.gis import admin
from .models import GeoData
# Register your models here.
admin.site.register(GeoData, admin.OSMGeoAdmin)