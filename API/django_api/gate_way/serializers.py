from rest_framework import serializers
from .models import jwttoken
 
class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()
  
class RegisterSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()
  name = serializers.CharField()
  
class RefreshSerializer(serializers.Serializer):
  refresh = serializers.CharField()