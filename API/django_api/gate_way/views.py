import jwt
import random, string
from rest_framework.serializers import Serializer
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from django.shortcuts import render
from .models import jwttoken
from user.models import CustomUser
from datetime import datetime, timedelta
from django.conf import settings
from .serializers import LoginSerializer, RefreshSerializer,RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .authentication import Authentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def get_random(N):
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def get_access_token(payload):
  return jwt.encode({ "exp": datetime.now() + timedelta(minutes=5),**payload },
  settings.SECRET_KEY ,
  algorithm="HS256"
  )

def get_refresh_token():
  return jwt.encode({ "exp": datetime.now() + timedelta(minutes=5), "data": get_random(10) },
  settings.SECRET_KEY ,
  algorithm="HS256"
  )
  

class LoginView(APIView): 
  serializer_class = LoginSerializer
  def post(self,request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(
    username=serializer.validated_data['email'],
    password=serializer.validated_data['password']
    )
    if not user:
      return Response({"error": "Invalid email address or password"}, status = "400")
    
    jwttoken.objects.filter(user_id=user.id).delete()
    access = get_access_token({"user_id":user.id})
    refresh = get_refresh_token()
    
    jwttoken.objects.create(
      user_id = user.id, access=access, refresh=refresh
    )
    return Response({"access": access.decode(), "refresh": refresh.decode()})
                        

class RegisterView(APIView):
  serializer_class = RegisterSerializer
  
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    CustomUser.objects._create_user(**serializer.validated_data)
    return Response({"success": "user registered successfully"})
 
 
def verify_token(token):
  try:
    decoded_data = jwt.decode(token,settings.SECRET_KEY,algorithm="HS256")
  except Exception:
    return None
  exp = decoded_data["exp"]
  if datetime.now().timestamp() > exp:
    return None
  return decoded_data
 
class RefreshView(APIView):
  serializer_class = RefreshSerializer
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    try:
      active_jwt = jwttoken.objects.get(refresh=serializer.validated_data["refresh"])
    except jwttoken.DoesNotExist:
      return Response({"error": "Refresh token not found"},status="400")
    refresh=serializer.validated_data["refresh"]

   #   if not Authentication.verify_token(refresh):
   #     return Response({"error": "Token is Invalid or expired"})
      
    access = get_access_token({"user_id": active_jwt.user.id})
    refresh = get_refresh_token()
    active_jwt.access = access.decode()
    active_jwt.refresh = refresh.decode()
    active_jwt.save()
    return Response({"access": access, "refresh": refresh})
  

  
class TestException(APIView):

  def get(self,request):
    print(request.user)
    return Response({"data":"this is secure"})