from django.db import models

from django.contrib.gis.db.models import PointField


# Create your models here.
class Geomessage(models.Model):
    point = PointField()
    message = models.CharField(max_length=200)
