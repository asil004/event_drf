from rest_framework import serializers

from .models import UserEvent, Event, EventDetail, Item, EventImage


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('image',)


class EventSerializer(serializers.ModelSerializer):
    event_images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetail
        fields = '__all__'


class UserEventSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    items = ItemsSerializer(many=True, read_only=True)
    event_detail = EventDetailSerializer()

    class Meta:
        model = UserEvent
        fields = ('id', 'is_active', 'event', 'items', 'event_detail')


class UserEventCreateSerializer(serializers.ModelSerializer):
    event_detail = EventDetailSerializer()

    class Meta:
        model = UserEvent
        fields = ('id', 'event', 'items', 'event_detail', 'total_sum')

# admin
