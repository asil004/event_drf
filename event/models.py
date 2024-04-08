from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to='event/')

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item/')

    def __str__(self):
        return str(self.name)


class EventImage(models.Model):
    image = models.ImageField(upload_to='event_img/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_images')

    def __str__(self):
        return str(self.event.name)


class EventDetail(models.Model):
    address = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.phone_number} {self.address} {self.date}"


class UserEvent(models.Model):
    user = models.ForeignKey(user, models.CASCADE, related_name='user_event')
    event = models.ForeignKey(Event, models.CASCADE, related_name='user_event')
    items = models.ManyToManyField(Item)
    event_detail = models.ForeignKey(EventDetail, models.CASCADE, related_name='user_event_detail')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name}, {self.event.name}, {self.event_detail.date}"
