import datetime

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.contrib.gis.geos import Point

from events_app.models import Event, User
from events_app.serializers import EventSerializer
from events_app import constants as c

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_event(description="", geo_location=None, author=None, creation_date=None, modify_date=None, state=0, category=0):
        states = [c.TO_VALIDATE, c.VALIDATED, c.RESOLVED]
        categories = [c.INCIDENT, c.CONSTRUNCTION, c.ROAD_CONDITION, c.SPECIAL_EVENT, c.WEATHER_CONDITION]
        
        if len(description) < 150 and geo_location != None and author != None and creation_date != None and \
            modify_date != None and state in states and category in categories:
            Event.objects.create(
                description=description,
                geo_location=geo_location,
                author=author,
                creation_date=creation_date,
                modify_date=modify_date,
                state=state,
                category=category
            )

    def setUp(self):
        self.create_event(
            "Aveiro Event",
            Point(-8.6455400, 40.6442700),
            User.objects.get(id=1),
            datetime.datetime.now(),
            datetime.datetime.now(),
            0,
            0
        )
        self.create_event(
            "Porto Event",
            Point(-8.6109900, 41.1496100),
            User.objects.get(id=2),
            datetime.datetime.now(),
            datetime.datetime.now(),
            0,
            1
        )
        self.create_event(
            "Lisboa Event",
            Point(-9.1333300, 38.7166700),
            User.objects.get(id=1),
            datetime.datetime.now(),
            datetime.datetime.now(),
            0,
            2
        )

class GetAllEventsTest(BaseViewTest):
    def test_get_all_events(self):
        c = self.client
        c.login(username="user", password="user")
        response = c.get(reverse("get_post_events"))

        expected_result = Event.objects.all()
        serialized = EventSerializer(expected_result, many=True)

        for e in serialized.data:
            e.pop('geo_location')

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
