from django.contrib.gis.db import models


# Create your models here.
class Geomessage(models.Model):
    point = models.PointField()
    message = models.CharField(max_length=200)
