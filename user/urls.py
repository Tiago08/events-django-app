from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'signup', UserViewSet, basename='signup')

urlpatterns =[
    path("user/", include(router.urls))
]