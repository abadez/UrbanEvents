import datetime

from rest_framework.response import Response
from rest_framework import mixins, generics
from django.contrib.gis.geos import Point

from events_app.models import Event
from events_app.serializers import EventSerializer
from events_app import constants as c

class EventsViewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request):
        if not request.user.is_authenticated:
            return Response('not authenticated!')

        return self.list(request)

    def post(self, request):
        if request.user.is_authenticated:
            request.data.update({
                'geo_location': Point(request.data['lon'], request.data['lat'], srid=4326), 
                'author': request.user.id,
                'creation_date': datetime.datetime.now(),
                'modify_date': datetime.datetime.now(),
                'state': c.TO_VALIDATE
            })
        else:
            return Response('not authenticated!')

        return self.create(request)

class EventsViewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response('not authenticated!')

        return self.retrieve(request)

    def put(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response('not authenticated!')
        elif not request.user.is_superuser:
            return Response('not an admin!')

        return self.update(request)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request)
