# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid

class Country(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class City(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

class Trip(models.Model):

    ON_WAY = 'onWay'
    NEAR = 'near'
    STARTED = 'started'

    STATUS_CHOICES = (
        (ON_WAY, ON_WAY),
        (NEAR, NEAR),
        (STARTED, STARTED),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        blank=True,
        null=True
    )

    price = models.FloatField(
        blank=True,
        null=True
    )

    start_date = models.DateTimeField(
        blank=True,
        null=True
    )

    end_date = models.DateTimeField(
        blank=True,
        null=True
    )


    start_pickup_address = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    start_pickup_location_type = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    start_pickup_location_latitude = models.FloatField(
        blank=True,
        null=True
    )

    start_pickup_location_longitude = models.FloatField(
        blank=True,
        null=True
    )

    end_pickup_address = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    end_pickup_location_type = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    end_pickup_location_latitude = models.FloatField(
        blank=True,
        null=True
    )

    end_pickup_location_longitude = models.FloatField(
        blank=True,
        null=True
    )

    passenger_first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    passenger_last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )


    driver_first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    driver_last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    driver_location_type = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    driver_location_latitude = models.FloatField(
        blank=True,
        null=True
    )

    driver_location_longitude = models.FloatField(
        blank=True,
        null=True
    )

    car_plate = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    check_code = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )

    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        unique=False,
        related_name='trips'
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        unique=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )