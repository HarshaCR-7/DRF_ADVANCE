from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer, UserProfileSerializer,CustomUser,UserProfile



# Create your views here.

class CustomUserViewSet(ModelViewSet):
  serializer_class = CustomUserSerializer
  queryset = CustomUser.objects.prefetch_related(
        "user_profile", "user_profile__address_info")


class UserProfileViewSet(ModelViewSet):
  serializer_class = UserProfileSerializer
  queryset = UserProfile.objects.select_related( "user","address_info")