from rest_framework import serializers
from .models import UserProfile,CustomUser, AddressGlobal


class AddressGlobalSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddressGlobal
    fields = ("address","city","state","country")

 
class CustomUserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = CustomUser
    fields = ("email","name","created_at","updated_at")
    
class UserProfileSerializer(serializers.ModelSerializer):
  user = CustomUserSerializer()
  address_info = AddressGlobalSerializer(read_only=True)

  class Meta:
    model = UserProfile
    fields = "__all__"