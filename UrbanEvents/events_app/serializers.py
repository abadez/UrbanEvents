from rest_framework import serializers

from events_app.models import Event
from events_app import constants as c

class EventSerializer(serializers.ModelSerializer):
    lat = serializers.SerializerMethodField()
    lon = serializers.SerializerMethodField()
    
    class Meta:
        model = Event
        fields = [
            'id',
            'description',
            'lat',
            'lon',
            'author',
            'creation_date',
            'modify_date',
            'state',
            'category'
        ]
        read_only_fields = ['id']

    '''
    def validate_state(self, value):
        if value not in [c.TO_VALIDATE, c.VALIDATED, c.RESOLVED]:
            raise serializers.ValidationError("Invalid state")

        return value

    def validate_category(self, value):
        if value not in [c.CONSTRUNCTION, c.INCIDENT, c.ROAD_CONDITION, c.SPECIAL_EVENT, c.WEATHER_CONDITION]:
            raise serializers.ValidationError("Invalid category")

        return value
    '''

    '''
    def create(self, data):
        return Event.objects.create(**data)
    '''

    def get_lat(self,data):
        return data.geo_location.x

    def get_lon(self,data):
        return data.geo_location.y

    '''
    def retrieve(self, data, *args, **kwargs):
        event = Event.objects.get(id=data['pk'])

        print("\nTTTTTTTT\n")

        return event
    '''