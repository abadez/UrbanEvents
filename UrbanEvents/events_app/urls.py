from django.urls import path

from events_app.views import EventsViewList, EventsViewDetail

urlpatterns = [
    path('events/', EventsViewList.as_view(), name="get_post_events"),
    path('events/<int:id>/', EventsViewDetail.as_view(), name="get_put_delete_events"),
]