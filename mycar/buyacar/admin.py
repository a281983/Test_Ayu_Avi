from django.contrib import admin

# Register your models here.
from .models import CarDesc
from .models import CarPrice

admin.site.register(CarDesc)
admin.site.register(CarPrice)