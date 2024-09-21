from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer, RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView

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
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_vlaid():
            user = serializer.save()