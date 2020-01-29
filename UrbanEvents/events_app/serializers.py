import datetime

from rest_framework import serializers

from events_app.models import Event
from events_app import constants as c

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'description', 
            'geo_location', 
            'author', 
            'creation_date', 
            'modify_date', 
            'state', 
            'category'
        ]
        read_only_fields = ['creation_date']

    def validate_state(self, value):
        if value not in [c.TO_VALIDATE, c.VALIDATED, c.RESOLVED]:
            raise serializers.ValidationError("Invalid state")

        return value

    def validate_category(self, value):
        if value not in [c.CONSTRUNCTION, c.INCIDENT, c.ROAD_CONDITION, c.SPECIAL_EVENT, c.WEATHER_CONDITION]:
            raise serializers.ValidationError("Invalid category")

    def create(self, data):
        
        print("BEFORE: " + str(data))
        
        data.update({
            'creation_date': datetime.datetime.now(),
            'modify_date': datetime.datetime.now(),
            'state': c.TO_VALIDATE
        })

        print("TESTE: " + str(data))

        return Event.objects.create(**data)