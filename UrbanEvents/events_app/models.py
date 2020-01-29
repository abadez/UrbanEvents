from django.contrib.gis.db import models
from django.contrib.auth.models import User

import events_app.constants as c

class Event(models.Model):
    description = models.CharField(max_length=100, null=False)
    geo_location = models.PointField(null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(null=False)
    modify_date = models.DateTimeField(null=True)
    state = models.IntegerField(default=c.TO_VALIDATE, null=False)
    category = models.IntegerField(null=False)

    def __str__(self):
        return self.description