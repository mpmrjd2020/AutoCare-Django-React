from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/vehicle/', views.VehicleListCreate.as_view(), name='vehicle_list' ),
    path('api/vehicle/<int:pk>', views.VehicleDetail.as_view(), name='vehicle_detail'),
    path('api/service/', views.ServiceListCreate.as_view(), name='service_log' ),
    path('api/service/<int:pk>', views.ServiceDetail.as_view(), name='service_detail'),
]