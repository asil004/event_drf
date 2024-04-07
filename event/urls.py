from django.urls import path, include

from event.views import UserEventListAPIView, UserEventCreateAPIView

urlpatterns = [
    path('event/', include([
        path('', UserEventListAPIView.as_view()),
        path('create/', UserEventCreateAPIView.as_view()),
    ])),
]
