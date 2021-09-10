from django.conf import settings
from django.db import models


class Vehicledetails(models.Model):
    "Generated Model"
    make = models.CharField(
        max_length=256,
    )
    price = models.FloatField(
        null=True,
        blank=True,
    )
    image = models.URLField(
        null=True,
        blank=True,
    )
    model = models.ForeignKey(
        "carapp.Carlist",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="vehicledetails_model",
    )


class Carlist(models.Model):
    "Generated Model"
    model = models.CharField(
        max_length=256,
    )


# Create your models here.
