from rest_framework import serializers, fields
from .models import Vehicle, Service_Log



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Log
        fields = ['vehicle', 'service_type', 'service_mileage', 'service_dt', 'service_by', 'service_receipt']

class VehicleSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'color', 'current_mileage', 'vehicle_image', 'services']

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        vehicle = Vehicle.objects.create(**validated_data)
        for service_data in services_data:
            Service_Log.objects.create(vehicle=vehicle, **service_data)
        return vehicle
   