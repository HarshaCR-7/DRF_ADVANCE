from django.shortcuts import render
from django.http import JsonResponse, response 
from .models import TestModel, Blog, Car
from .serializers import SimpleSerializer
from rest_framework import viewsets
from django_seed import Seed
from random import randint

car_name=["Mercedes","toyota","Audi","Nissan","Honda",]
seeder = Seed.seeder()
seeder.add_entity(Blog, 20)
#seeder.add_entity(Car, 100, {
#  'name': lambda x: car_name[randint(0,len(car_name) - 1)]
#})

def execute():
  seeder.execute()
  #seeder1.execute()
  print("Success seeding")




class SimpleViewset(viewsets.ModelViewSet):
  queryset = TestModel.objects.all()
  serializer_class = SimpleSerializer
