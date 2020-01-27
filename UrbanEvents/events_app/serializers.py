from rest_framework import serializers

from models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['description', 'geo_location', 'author', 'creation_date', 'modify_date', 'state', 'category']