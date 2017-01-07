from __future__ import unicode_literals

from django.db import models

# Create your models here.
#!I&hXSKu)6Ft
#'avinashmehrotra'@'localhost'
#Avinash123


class CarDesc(models.Model):    
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    yom = models.CharField(max_length=200)
    mom = models.CharField(max_length=200)
    mileage = models.PositiveIntegerField()
    doors_num = models.PositiveSmallIntegerField()
    seats_num = models.PositiveSmallIntegerField()
    gear = models.CharField(max_length=200)
    drive = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=200)
    Acc_Music = models.CharField(max_length=200)
    Acc_Keys = models.CharField(max_length=200)
    Acc_Roof = models.CharField(max_length=200)
    Acc_Seats = models.CharField(max_length=200)
    Acc_Lights = models.CharField(max_length=200)


class CarPrice(models.Model):
    carprice = models.CharField(max_length=200)
    maxdiscount = models.CharField(max_length=200)