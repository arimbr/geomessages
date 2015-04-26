from django.shortcuts import render, HttpResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from rest_framework.renderers import JSONRenderer

from .models import Geomessage
from .serializers import GeomessageSerializer


# Create your views here.
def message_list(request):
    # Get access to URL query parameters
    # /api/v1/messages/?lat=66.434&lng=44.3453
    lat = request.GET.get('lat') or 0
    lng = request.GET.get('lng') or 0
    origin = Point(float(lat), float(lng))

    # Find geomessages that are within 1000 km from the user location
    qs = Geomessage.objects.filter(location__distance_lte=(origin, D(km=1000)))
    serializer = GeomessageSerializer(qs, many=True)
    json_content = JSONRenderer().render(serializer.data)

    return HttpResponse(content=json_content)
