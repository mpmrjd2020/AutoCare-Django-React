from rest_framework import serializers, fields
from .models import Vehicle, Service_Log



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Log
        fields = ['id', 'vehicle', 'service_type', 'service_mileage', 'service_dt', 'service_by', 'service_receipt']
        read_only_fields = ('vehicle',)


class VehicleSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'model', 'year', 'color', 'current_mileage', 'vehicle_image', 'services']

    def create(self, validated_data):
        print(validated_data)
        services_data = validated_data.pop('services')
        vehicle = Vehicle.objects.create(**validated_data)
        print(vehicle)
        print(services_data)
        for service_data in services_data:
            Service_Log.objects.create(vehicle=vehicle, **service_data)
        return vehicle
       
    def update(self, instance, validated_data):
        services_data = validated_data.pop('services')
        services = (instance.services).all()
        services = list(services)
        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.color = validated_data.get('color', instance.color)
        instance.current_mileage = validated_data.get('current_mileage', instance.current_mileage)
        instance.vehicle_image = validated_data.get('vehicle_image', instance.vehicle_image)
        instance.save()

        for service_data in services_data:
            service = services.pop(0)
            service.service_type = service_data.get('service_type', service.service_type)
            service.service_mileage = service_data.get('service_mileage', service.service_mileage)
            service.service_dt = service_data.get('service_dt', service.service_dt)
            service.service_by = service_data.get('service_by', service.service_by)
            # service.service_receipt = service_data.get('service_receipt', service_receipt)
            service.save()
        return instance