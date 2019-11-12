# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Vehicle(models.Model):
    plate = models.CharField(max_length=120)

class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.DecimalField(max_digits=30, decimal_places=27)
    longitude = models.DecimalField(max_digits=30, decimal_places=27)
