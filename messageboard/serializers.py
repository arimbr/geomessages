from rest_framework_gis import serializers

from .models import Geomessage


class GeomessageSerializer(serializers.GeoModelSerializer):

    class Meta:
        model = Geomessage
        geo_field = 'point'

        fields = ('message', 'location', 'date')
