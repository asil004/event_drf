from django.urls import path, include, re_path
from .views import ChangePasswordView, RegisterView, MyObtainTokenPairView, LogoutAPIView, ForgotPasswordView, \
    VerifyCodeView, UserUpdatenameView, AdminUpdatenameView, AdminLoginView
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
        path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
        path('send_gmail_code/', ForgotPasswordView.as_view(), name='forgot_password'),
        path('code_check/', VerifyCodeView.as_view(), name='verification_code'),
        path('user_update_name/',UserUpdatenameView.as_view(), name='user_update_name'),
        path('admin_update_name/',AdminUpdatenameView.as_view(), name='admin_update_name'),
        path('admin_login/', AdminLoginView.as_view(), name='admin_login')
    ])),

]
