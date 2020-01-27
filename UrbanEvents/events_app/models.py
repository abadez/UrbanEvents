from django.db import models

import constants as c

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    geo_location = models.IntegerField()
    author = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
    modify_date = models.DateTimeField()
    state = models.IntegerField(default=c.TO_VALIDATE)
    category = models.IntegerField()