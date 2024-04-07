from rest_framework import serializers

from .models import UserEvent, Event, EventDetail, Item


class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = '__all__'
