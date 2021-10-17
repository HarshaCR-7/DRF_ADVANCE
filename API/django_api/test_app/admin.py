
from django.contrib import admin
from .models import Car, ModelX, ModelY, TestModel, Blog

# Register your models here.
admin.site.register(TestModel)
admin.site.register(ModelX)
admin.site.register(ModelY)
admin.site.register(Blog)
admin.site.register(Car)