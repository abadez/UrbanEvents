from django.urls import path

from events_app.views import EventsView

urlpatterns = [
    path('all_events/', EventsView.as_view()),
]