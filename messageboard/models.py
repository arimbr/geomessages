from django.contrib.gis.db import models


# Create your models here.
class Geomessage(models.Model):
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    location = models.PointField()
