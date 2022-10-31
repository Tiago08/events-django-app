from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import EventBookingSerializer, EventSerializer
from .models import EventBooking, Event, Room


class EventViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.filter(event_type='public')

class EventBookingViewSet(viewsets.ModelViewSet):
    serializer_class = EventBookingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if self.request.user.id != int(request.data['user_id']):
            return Response({"Error": "you can not book event for another user."}, status=status.HTTP_403_FORBIDDEN)
        if EventBooking.objects.filter(user=request.data['user_id']).filter(event_id=request.data['event_id']).exists():
            return Response({"Error": "You have already booked that event"}, status=status.HTTP_400_BAD_REQUEST)
        data = self.request.data
        serializer = EventBookingSerializer(data=data)
        if serializer.is_valid():
            event = Event.objects.filter(id=data['event_id']).first()
            if event:
                if event.event_type == 'private':
                    return Response({"Error": "This is private event"}, status=status.HTTP_403_FORBIDDEN)
            room = Room.objects.get(id=event.room.id)
            if room.capacity < 1:
                return Response({"Error": "No space available"}, status=status.HTTP_403_FORBIDDEN)
            room.capacity -= 1
            room.save()
            serializer.save(is_booked=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return EventBooking.objects.filter(user=self.request.user).filter(is_deleted=False)