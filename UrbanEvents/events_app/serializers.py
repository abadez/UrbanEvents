from rest_framework import serializers

from events_app.models import Event
from events_app import constants as c

class EventSerializer(serializers.ModelSerializer):
    # Latitude
    lat = serializers.SerializerMethodField()
    # Longitude
    lon = serializers.SerializerMethodField()
    
    class Meta:
        model = Event
        fields = [
            'id',
            'description',
            'geo_location',
            'lat',
            'lon',
            'author',
            'creation_date',
            'modify_date',
            'state',
            'category'
        ]
        read_only_fields = ['id']

    def validate_description(self, value):
        if len(value) > 150:
            raise serializers.ValidationError("Invalid description")

        return value

    def validate_state(self, value):
        if value not in [c.TO_VALIDATE, c.VALIDATED, c.RESOLVED]:
            raise serializers.ValidationError("Invalid state")

        return value

    def validate_category(self, value):
        if value not in [c.CONSTRUNCTION, c.INCIDENT, c.ROAD_CONDITION, c.SPECIAL_EVENT, c.WEATHER_CONDITION]:
            raise serializers.ValidationError("Invalid category")

        return value

    def get_lat(self,data):
        return data.geo_location.y

    def get_lon(self,data):
        return data.geo_location.x
