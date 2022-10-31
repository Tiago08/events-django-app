from django.urls import path, include
from rest_framework import routers
from .views import EventBookingViewSet, EventViewSet


router = routers.DefaultRouter()
router.register(r'booking', EventBookingViewSet, basename='booking')
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls))
]