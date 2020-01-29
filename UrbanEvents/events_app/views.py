from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from events_app.models import Event
from events_app.serializers import EventSerializer

class EventsView(mixins.CreateModelMixin, generics.ListAPIView):
    #lookup_field = 'pk'
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

    def get(self, request):
        events = Event.objects.all()
        serializer_class = EventSerializer(events, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        if request.user.is_authenticated:
            request.data['author'] = request.user.id
        else:
            return Response('not authenticated!')

        print("REQUEST_DATA: " + str(request.data))

        return self.create(request)