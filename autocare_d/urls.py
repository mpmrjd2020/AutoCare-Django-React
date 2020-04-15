from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/vehicle/', views.VehicleListCreate.as_view(), name='vehicle_list' ),
    path('api/service/', views.ServiceListCreate.as_view(), name='service_log' ),
]