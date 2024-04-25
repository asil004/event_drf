from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import *
from .serializers import UserEventSerializer, UserEventCreateSerializer, ItemsSerializer, \
    EventSerializer


class UserEventListAPIView(ListAPIView):
    permission_class = IsAuthenticated
    serializer_class = UserEventSerializer

    def get_queryset(self):
        return UserEvent.objects.filter(user=self.request.user)


class UserEventCreateAPIView(CreateAPIView):
    permission_class = IsAuthenticated
    serializer_class = UserEventCreateSerializer

    def perform_create(self, serializer):
        # Get the event details from the request
        event_details = self.request.data.get('event_detail')
        # Assuming 'event_detail' contains necessary information to create an Event object
        # Create the Event object
        event = EventDetail.objects.create(**event_details)

        # # Set the user for the event as the current authenticated user
        # event.user = self.request.user

        # Save the event object
        serializer.save(user=self.request.user, event_detail=event)


#####
class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer


# admin
class AdminEventsListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserEvent.objects.filter(is_active=True)
    serializer_class = UserEventSerializer


class AdminEventsHistoryListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserEvent.objects.filter(is_active=False)
    serializer_class = UserEventSerializer


class AdminUpcomingUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):

        try:
            user_event = UserEvent.objects.get(id=pk, is_active=True)
        except Exception as e:
            return Response({"detail": f"UserEvent not found e-> {e}"}, status=status.HTTP_404_NOT_FOUND)

        # update user_event is_active to False
        user_event.is_active = False
        user_event.save()

        return Response({"detail": f"UserEvent successfully finished"}, status=status.HTTP_200_OK)


class AdminHistoryDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        try:
            user_event = UserEvent.objects.filter(id=pk, is_active=False)
        except Exception as e:
            return Response({"detail": f"UserEvent not found or is_active is True e-> {e}"},
                            status=status.HTTP_404_NOT_FOUND)

        user_event.delete()
        return Response({"detail": f"UserEvent successfully deleted"}, status=status.HTTP_200_OK)
