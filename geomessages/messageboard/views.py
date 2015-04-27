from django.shortcuts import HttpResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from rest_framework.renderers import JSONRenderer

from .models import Geomessage
from .serializers import GeomessageSerializer


# Create your views here.
def message_list(request):
    # Get access to URL query parameters
    # /api/v1/messages/?lat=66.434&lng=66.3453
    lat = request.GET.get('lat') or 0
    lng = request.GET.get('lng') or 0
    origin = Point(float(lat), float(lng))

    # Find geomessages that are within 50 km from the user location
    qs = Geomessage.objects.filter(location__distance_lte=(origin, D(km=50)))
    # TODO: qs stills need to be ordered by distance
    serializer = GeomessageSerializer(qs, many=True)
    json_content = JSONRenderer().render(serializer.data)

    return HttpResponse(content=json_content)
