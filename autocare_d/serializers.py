from rest_framework import serializers
from .models import Vehicle, Service_log

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('make', 'model', 'year', 'color', 'current_mileage', 'vehicle_image')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('vehicle', 'service_type', 'service_mileage', 'service_dt', 'service_by', 'service_receipt')

    