from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer, RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from django.contrib.auth.models import User
import environ
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

# env setup
env = environ.Env()
environ.Env.read_env()

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset

class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_vlaid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            full_name = f'{user.first_name} {user.last_name}'
            confirm_url = f'http://127.0.0.1:8000/user/confirm/{uid}/{token}/'
            email_subject = 'Confirm Your Account'
            email_body = render_to_string('users/confirm_account_mail.html', {'confirm_url': confirm_url, 'full_name': full_name})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response({'message': 'We have sent you a link to confirm your account. Please check your email'}, status=200)
        else:
            return Response(serializer.errors, status=400)

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        Customer(user=user).save()
        return redirect(env("ClIENT_URL")+"/login")
    else:
        return Response(env("ClIENT_URL")+"/register")

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                if user.is_staff:
                    return Response({'token': token.key, 'user_id': user.pk, 'admin': True}, status=200)
                else:
                    return Response({'token': token.key, 'user_id': user.pk}, status=200)
        else:
            return Response({'message': 'Username or password is incorrect'}, status=400)

class LogoutView(APIView):
    def get(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'Logout successful'}, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=500)