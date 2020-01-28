from django.urls import path

from events_app.views import EventsView

urlpatterns = [
    path('events/', EventsView.as_view(), name="get_events"),
]