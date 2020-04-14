from django.db import models

# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=50)
    current_mileage = models.CharField(max_length=10)
    vehicle_image = models.TextField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeZ5dDmSiPUes1VyS31ITsH2xoMFV8_ihiAQdC9BuCMWkevRXo&usqp=CAU')

    def __str__(self):
        return self.make

class Service_Log(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='Service_Log')
    service_type = models.CharField(max_length=200)
    service_mileage = models.CharField(max_length=10)
    service_dt = models.CharField(max_length=50)
    service_by = models.CharField(max_length=200)
    service_receipt = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.service_type
