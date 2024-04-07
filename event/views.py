from django.forms import model_to_dict
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import UserEventSerializer, UserEventCreateSerializer, EventDetailSerializer, ItemsSerializer, \
    EventSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserEventListAPIView(ListAPIView):
    permission_class = IsAuthenticated
    serializer_class = UserEventSerializer

    def get_queryset(self):
        return UserEvent.objects.filter(user=self.request.user)


class UserEventCreateAPIView(CreateAPIView):
    permission_class = IsAuthenticated
    serializer_class = UserEventCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        event_detail = EventDetail.objects.create(user=user)
        serializer.save(event_detail=event_detail)
