from django.db import models
from django.contrib.auth.models import User


class EventType(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    info = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_type)
