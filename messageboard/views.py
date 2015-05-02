from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Geomessage
from .serializers import GeomessageSerializer


@api_view(['GET', 'POST'])
def message_list(request):
    """
    List all messages, or create a new message
    GET /api/v1/messages/?lat=66.434&lng=66.3453
    POST content
    {
        "message": "I wish Finnish people would gather outdoors together more often, like in Vappu",
        "location": { "type": "Point", "coordinates": [ 60.1708, 24.9375 ] }
    }
    """
    if request.method == 'GET':
        # Get URL query parameters
        lat = request.GET.get('lat') or 0
        lng = request.GET.get('lng') or 0
        origin = Point(float(lat), float(lng))

        # Return messages within 50 km from user location ordered by distance
        messages = Geomessage.objects.filter(
            location__distance_lte=(origin, D(km=50)))
        messages = messages.distance(origin).order_by('distance')
        serializer = GeomessageSerializer(messages, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GeomessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
