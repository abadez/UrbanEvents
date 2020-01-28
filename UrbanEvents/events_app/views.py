from rest_framework.response import Response
from rest_framework.views import APIView
from events_app.models import Event

class EventsView(APIView):
    def get(self, request):
        events = Event.objects.all()
        return Response({'events': events})