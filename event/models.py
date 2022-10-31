from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255, choices=(('public', 'Public'), ('private', 'Private')))
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='event_room')
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.event_name


class EventBooking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    is_booked = models.BooleanField(default=True)
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.event.event_name

    def save(self, *args, **kwargs):
        if self.is_cancelled:
            event = Event.objects.get(id=self.event.id)
            room = Room.objects.get(id=event.room.id)
            room.capacity += 1
            room.save()
            self.is_booked = False
        super().save(*args, **kwargs)

