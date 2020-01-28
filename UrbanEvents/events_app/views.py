from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from events_app.models import Event
from events_app.serializers import EventSerializer

class EventsView(mixins.CreateModelMixin, generics.ListAPIView):
    #lookup_field = 'pk'
    serializer_class = EventSerializer

    def get(self, request):
        events = Event.objects.all()
        serializer_class = EventSerializer(events, many=True)
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)