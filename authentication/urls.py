from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView,PasswordValidator,UsernameValidor,EmailValidator,GetEmail
urlpatterns = [
    path('', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('password-validate/', PasswordValidator.as_view()),
    path('username-validate/', UsernameValidor.as_view()),
    path('email-validate/', EmailValidator.as_view()),
    path('send-email/', GetEmail.as_view()),
]