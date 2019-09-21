from django.contrib.gis.db import models


class GeoData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    geom = models.PolygonField()
