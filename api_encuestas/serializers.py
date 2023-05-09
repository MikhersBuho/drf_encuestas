from rest_framework import serializers
from .models import company, domain
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', "password", "first_name", "last_name", "is_active", "user_permissions"]
        # fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'
        
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = domain
        fields = '__all__'