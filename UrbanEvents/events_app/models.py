from django.db import models
from django.contrib.auth.models import User

import events_app.constants as c

class Author(models.Model):
    

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, null=True)
    geo_location = models.IntegerField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(null=True)
    modify_date = models.DateTimeField(null=True)
    state = models.IntegerField(default=c.TO_VALIDATE, null=False)
    category = models.IntegerField(null=True)

    def __str__(self):
        return self.description