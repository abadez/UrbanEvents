from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from events_app.models import Event
from events_app.serializers import EventSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_event(location=-1, author=""):
        if location != -1 and author != "":
            Event.objects.create(geo_location=location, author=author)

    def setUp(self):
        self.create_event(0, "teste")
        self.create_event(1, "teste1")
        self.create_event(2, "teste2")

class GetAllEventsTest(BaseViewTest):
    def test_get_all_events(self):
        response = self.client.get(reverse("events"))

        expected_result = Event.objects.all()
        serialized = EventSerializer(expected_result, many=True)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

