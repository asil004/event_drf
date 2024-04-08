from django.urls import path, include, re_path
from .views import ChangePasswordView, UpdateProfileView, RegisterView, MyObtainTokenPairView, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('auth/', include([
        path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
        path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('register/', RegisterView.as_view(), name='auth_register'),
        path('logout/', LogoutAPIView.as_view(), name="logout"),
        re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        # change
        path('change_password/<int:id>', ChangePasswordView.as_view(), name='auth_change_password'),
        path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
    ])),

]
