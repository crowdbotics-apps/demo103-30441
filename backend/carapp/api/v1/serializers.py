from rest_framework import serializers
from carapp.models import Carlist, Vehicledetails


class VehicledetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicledetails
        fields = "__all__"


class CarlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carlist
        fields = "__all__"
