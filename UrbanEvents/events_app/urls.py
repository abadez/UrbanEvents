from django.urls import path

from events_app.views import EventsViewList, EventsViewDetail

urlpatterns = [
    path('events/', EventsViewList.as_view(), name="get_events"),
    path('events/<int:pk>/', EventsViewDetail.as_view(), name="change_events"),
]