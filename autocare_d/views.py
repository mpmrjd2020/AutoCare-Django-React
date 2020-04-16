from django.shortcuts import render
from .models import Vehicle, Service_Log
from .serializers import VehicleSerializer, ServiceSerializer
from rest_framework import generics



# Create your views here.
class VehicleListCreate(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
        
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service_Log.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service_Log.objects.all()

