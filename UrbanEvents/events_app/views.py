import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from events_app.models import Event
from events_app.serializers import EventSerializer
from events_app import constants as c

class EventsViewList(APIView):
    def get(self, request):
        # Request must be authorized
        if not request.user.is_authenticated:
            return Response('User not authenticated!', status=status.HTTP_401_UNAUTHORIZED)

        events = Event.objects.all()

        # if author filter
        author = request.query_params.get('author')
        if author:
            events = events.filter(author=int(author))

        # if category filter
        category = request.query_params.get('category')
        if category:
            events = events.filter(category=int(category))

        # if geo_location filter
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        radius = request.query_params.get('r')
        if lat and lon and radius:
            events = events.filter(geo_location__distance_lt=(Point(float(lon), float(lat)), Distance(km=radius)))

        serializer = EventSerializer(events, many=True)

        # Remove geo_location from response
        for s in serializer.data:
            s.pop('geo_location')

        return Response(serializer.data)

    def post(self, request):
        # Request must be authorized
        if not request.user.is_authenticated:
            return Response('User not authenticated!', status=status.HTTP_401_UNAUTHORIZED)

        # Update data with missing fields
        request.data.update({
                'geo_location': Point(request.data['lon'], request.data['lat']), 
                'author': request.user.id,
                'creation_date': datetime.datetime.now(),
                'modify_date': datetime.datetime.now(),
                'state': c.TO_VALIDATE
            })

        serializer = EventSerializer(data=request.data)
        
        # Save event if valid
        if serializer.is_valid():
            serializer.save()

            # Remove geo_location from response
            to_return = serializer.data
            to_return.pop('geo_location')

            return Response(to_return, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventsViewDetail(APIView):
    def get(self, request, id):
        # Request must be authorized
        if not request.user.is_authenticated:
            return Response('User not authenticated!', status=status.HTTP_401_UNAUTHORIZED)

        # Try to get requested event
        event = None
        try:
            event = Event.objects.get(id=id)
        except Event.DoesNotExist:
            return Response('Event not found!', status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event)

        # Remove geo_location from response
        to_return = serializer.data
        to_return.pop('geo_location')

        return Response(to_return, status=status.HTTP_200_OK)

    def put(self, request, id):
        # Request must be from an admin
        if not request.user.is_superuser:
            return Response('User not authorized!', status=status.HTTP_403_FORBIDDEN)

        # Try to get requested event
        event = None
        try:
            event = Event.objects.get(id=id)
        except Event.DoesNotExist:
            return Response('Event not found!', status=status.HTTP_404_NOT_FOUND)
        
        # Update data to save
        serializer = EventSerializer(event)
        event_data = serializer.data
        event_data['modify_date'] = datetime.datetime.now()
        event_data['state'] = request.data['state']

        serializer = EventSerializer(event, data=event_data)

        # Update event if request data is valid
        if serializer.is_valid():
            serializer.save()

            # Remove geo_location from response
            to_return = serializer.data
            to_return.pop('geo_location')

            return Response(to_return, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        # Request must be from an admin
        if not request.user.is_superuser:
            return Response('User not authorized!', status=status.HTTP_403_FORBIDDEN)

        # Try to get request event
        event = None
        try:
            event = Event.objects.get(id=id)
        except Event.DoesNotExist:
            return Response('Event not found!', status=status.HTTP_404_NOT_FOUND)

        # Delete event
        event.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
