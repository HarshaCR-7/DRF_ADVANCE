from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title


class Car(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.name
  





class TestModel(models.Model):
  name = models.CharField(max_length=255,null=True,blank=True , unique=True, error_messages={"null":"THis field cannot be empty", "unique":"Name already exist"})
  description = models.TextField(max_length=555)
  phone_number = models.PositiveIntegerField(unique=True)
  is_live = models.BooleanField()
  amount = models.FloatField()
  exta_name = models.CharField(max_length=255,editable=False, default="null")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    ordering = ['id']
    verbose_name_plural ="Test Model"
  def __str__(self):
    return f"{self.exta_name}"
  def save(self,*args,**kwargs):
    self.exta_name = f"{self.name}"
    super().save(*args,**kwargs)
    
    
    
class ModelX(models.Model):
  test_content = models.ForeignKey(TestModel, related_name="test_context" ,on_delete=models.CASCADE)
  mileage = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    ordering = ['created_at']
  def __str__(self):
    return f"{self.test_content.name}-{self.mileage}"
  
  
   
class ModelY(models.Model):
  test_content = models.OneToOneField(TestModel, related_name="test_context_y" ,on_delete=models.CASCADE)
  mileage = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    ordering = ['created_at']
  def __str__(self):
    return f"{self.test_content.name}-{self.mileage}"
  