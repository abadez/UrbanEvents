from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('events_api/', include('events_app.urls')),
    path('admin/', admin.site.urls),
]