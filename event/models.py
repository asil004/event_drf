from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item/')

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to='event/')
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='event_items')

    def __str__(self):
        return str(self.name)


class EventDetail(models.Model):
    address = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    phone_number = models.CharField(max_length=15)


class UserEvent(models.Model):
    user = models.ForeignKey(user, models.CASCADE, related_name='user_event')
    event = models.ForeignKey(Event, models.PROTECT, related_name='user_event')
    event_detail = models.ForeignKey(EventDetail, models.PROTECT, related_name='user_event_detail')
