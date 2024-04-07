from django.urls import path, include

from event.views import UserEventListAPIView


class UserEventCreateAPIView:
    pass


urlpatterns = [
    path('event/', include([
        path('', UserEventListAPIView.as_view()),
        # path('/', UserEventCreateAPIView.as_view()),
    ])),
]
