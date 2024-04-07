from django.test import TestCase
from django.urls import path, include
from .views import ChangePasswordView, UpdateProfileView, RegisterView, MyObtainTokenPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('auth/', include([
        path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
        path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('register/', RegisterView.as_view(), name='auth_register'),
        path('drf-auth/', include('rest_framework.urls')),

        # change
        path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
        path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
    ])),

]
