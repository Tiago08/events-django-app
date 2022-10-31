from rest_framework import serializers
from .models import EventBooking, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "event_name", "event_type", "created_at")


class EventBookingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField(read_only=True)
    event_id = serializers.IntegerField(write_only=True)
    event = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EventBooking
        fields = ('id', 'user_id', 'user', 'event_id', 'event', 'is_booked', 'is_cancelled', 'created_at')
