from django.urls import path, include

from event.views import UserEventListAPIView, UserEventCreateAPIView, EventListAPIView, ItemListAPIView, \
    AdminEventsListAPIView, AdminUpcomingUpdateAPIView, AdminEventsHistoryListAPIView, AdminHistoryDeleteAPIView

urlpatterns = [
    path('user-event/', include([
        path('', UserEventListAPIView.as_view()),
        path('create/', UserEventCreateAPIView.as_view()),
    ])),
    path('event/', include([
        path('', EventListAPIView.as_view()),
        path('items/', ItemListAPIView.as_view()),
    ])),
    path('admin/', include([
        path('upcoming/', AdminEventsListAPIView.as_view()),
        path('history/', AdminEventsHistoryListAPIView.as_view()),
        path('upcoming-finish/<int:pk>', AdminUpcomingUpdateAPIView.as_view()),
        path('history-delete/<int:pk>', AdminHistoryDeleteAPIView.as_view()),
    ])),
]
