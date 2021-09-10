from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CarlistViewSet, VehicledetailsViewSet

router = DefaultRouter()
router.register("vehicledetails", VehicledetailsViewSet)
router.register("carlist", CarlistViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
