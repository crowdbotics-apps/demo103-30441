from rest_framework import authentication
from carapp.models import Carlist, Vehicledetails
from .serializers import CarlistSerializer, VehicledetailsSerializer
from rest_framework import viewsets


class VehicledetailsViewSet(viewsets.ModelViewSet):
    serializer_class = VehicledetailsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Vehicledetails.objects.all()


class CarlistViewSet(viewsets.ModelViewSet):
    serializer_class = CarlistSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Carlist.objects.all()
