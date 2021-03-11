from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from rest_framework.authentication import TokenAuthentication
from event.models import EventType, Event
from event.serializers import EventSerializers, UserSerializers
from rest_framework import permissions


# class EventTypeViewSet(viewsets.ModelViewSet):
#     queryset = EventType.objects.all()
#     serializer_class = EventTypeSerializers


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = (permissions.AllowAny, )

class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializers


