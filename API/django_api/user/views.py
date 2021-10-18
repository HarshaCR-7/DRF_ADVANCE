from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer, UserProfileSerializer,CustomUser,UserProfile



# Create your views here.

class CustomUserViewSet(ModelViewSet):
  serializer_class = CustomUserSerializer
  queryset = CustomUser.objects.all()

class UserProfileViewSet(ModelViewSet):
  serializer_class = UserProfileSerializer
  queryset = UserProfile.objects.all()
