from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import UserEventSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserEventListAPIView(ListAPIView):
    permission_classes = IsAuthenticated
    serializer_class = UserEventSerializer

    def get_queryset(self):
        return UserEvent.objects.filter(user=self.request.user)
