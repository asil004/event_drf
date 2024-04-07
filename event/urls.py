from django.urls import path, include

urlpatterns = [
    path('event/', include([
        path('/', UserEventListAPIView.as_view()),
        path('/', UserEventCreateAPIView.as_view()),
    ])),
]
