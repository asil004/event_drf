from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ChangePasswordSerializer, \
    RegisterSerializer, MyTokenObtainPairSerializer, LogoutSerializer, ForgotPasswordSerializer, CodeCheckSerializer, \
    UserSerializer, AdminSerializer, AdminLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.core.mail import send_mail
import smtplib
import ssl
from django.conf import settings

import random


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            "message": "User registered successfully.",
            "refresh": str(refresh),
            "access": str(access)
        }, status=status.HTTP_201_CREATED)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


# change user
class ChangePasswordView(APIView):
    serializer_class = ChangePasswordSerializer

    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            password2 = serializer.validated_data.get('password2')

            User = get_user_model()
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "User with provided email does not exist."},
                                status=status.HTTP_404_NOT_FOUND)

            if password != password2:
                return Response({"detail": "Password fields didn't match."},
                                status=status.HTTP_400_BAD_REQUEST)

            user.set_password(password)
            user.save()

            return Response({"detail": "Password updated successfully."})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=LogoutSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ForgotPasswordView(APIView):

    @swagger_auto_schema(request_body=ForgotPasswordSerializer)
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'message': 'Foydalanuvchi topilmadi'}, status=status.HTTP_404_NOT_FOUND)

            # Parolni tiklash uchun kod yaratish
            code = ''.join(random.choices('0123456789', k=6))
            user.gmail_code = code
            user.save()

            # Email yuborish
            context = ssl.create_default_context()
            port = 465
            sender_email = 'sardor_shukurov2003S@mail.ru'
            password = 'dgm20y86ReJZXSEpvphz'  # Bu o'zgaruvchini o'zgartiring
            with smtplib.SMTP_SSL("smtp.mail.ru", port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, [email], f'Sizning parolni tiklash uchun kod: {code}')

            return Response({'message': 'Parolni tiklash uchun kod yuborildi'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):

    @swagger_auto_schema(request_body=CodeCheckSerializer)
    def post(self, request):
        code = request.data.get('code')  # Foydalanuvchi kiritgan kod
        user = User.objects.filter(gmail_code=code).first()  # Kodni tekshirish

        if user:  # Agar kod to'g'ri bo'lsa
            return Response({'message': 'Ok code'}, status=status.HTTP_200_OK)
        else:  # Agar kod noto'g'ri bo'lsa yoki topilmagan bo'lsa
            return Response({'message': 'Error kod'}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdatenameView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            new_first_name = serializer.validated_data.get('first_name')
            user.first_name = new_first_name
            user.save()
            return Response({'message': 'Ism muvaffaqiyatli o\'zgartirildi'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminUpdatenameView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            new_first_name = serializer.validated_data.get('first_name')
            user.first_name = new_first_name
            new_last_name = serializer.validated_data.get('last_name')
            user.last_name = new_last_name
            user.save()
            return Response({'message': 'Ism va familya o\'zgartirildi'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AdminLoginSerializer
