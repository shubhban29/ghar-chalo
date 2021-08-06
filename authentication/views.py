import datetime
from django.db import models
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from authentication.models import User
import time
from datetime import date
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .serializers import RegistrationSerializer, LoginSerializer,UserSerializer
from .renderers import UserJSONRenderer
from .utils import check_username,password_check,validate_email
from django.core.mail import send_mail
# Create your views here.
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PasswordValidator(APIView):
    def post(self, request):
        try:
            password = password_check(request.data['password'])
            return Response({"message":"password is valid"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail[0]}, status=status.HTTP_400_BAD_REQUEST)

class UsernameValidor(APIView):
    def post(self, request):
        try:
            username = check_username(request.data['name'],request.data['username'])
            return Response({"message":"username is valid"}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail[0]}, status=status.HTTP_400_BAD_REQUEST)

class EmailValidator(APIView):
    def post(self, request, *args, **kwargs):
        try:
            email = validate_email(request.data['name'],request.data['email'])
            return Response({"message":"email is valid"},status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail[0]}, status=status.HTTP_400_BAD_REQUEST)

class GetEmail(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        for i in range(3):
            send_mail('Welcome to Ghar chalo', 'Welcome to Ghar chalo','skrkmk212@gmail.com',[email])
        return Response({"message":"successfully sended email"})

