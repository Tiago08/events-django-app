from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.none()
