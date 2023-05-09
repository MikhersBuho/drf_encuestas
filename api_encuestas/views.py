# from django.shortcuts import render
from .models import domain, company
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import  UserSerializer, DomainSerializer, CompanySerializer
from rest_framework import viewsets, permissions

# Create your views here.

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if not serializer.validated_data.get('username'):
            # Si el campo 'username' no se proporcionó en la solicitud,
            # se utiliza el valor del campo 'email' para llenarlo.
            username = serializer.validated_data['email']
            serializer.validated_data['username'] = username
        # Llamada al método 'create' del serializador para guardar el objeto 'User' en la base de datos.
        serializer.save()

class CompanyList(viewsets.ModelViewSet):
    queryset = company.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanySerializer

class DomainList(viewsets.ModelViewSet):
    queryset = domain.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DomainSerializer