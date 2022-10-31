from django.contrib import admin
from .models import Room, Event, EventBooking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_name", "capacity")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_name", "room")


@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ("event", "user")