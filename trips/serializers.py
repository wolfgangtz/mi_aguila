from rest_framework import serializers
from trips.models import Country
from trips.models import City
from trips.models import Trip


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            'id',
            'name'
        )


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            'id',
            'name'
        )


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = (
            'id',
            'status',
            'price',
            'start_date',
            'end_date',
            'start_pickup_address',
            'start_pickup_location_type',
            'start_pickup_location_latitude',
            'start_pickup_location_longitude',
            'end_pickup_address',
            'end_pickup_location_type',
            'end_pickup_location_latitude',
            'end_pickup_location_longitude',
            'passenger_first_name',
            'passenger_last_name',
            'driver_first_name',
            'driver_last_name',
            'driver_location_type',
            'driver_location_latitude',
            'driver_location_longitude',
            'car_plate',
            'check_code',
            'city',
            'country'
        )


class TripByCitySerializer(serializers.ModelSerializer):

    trips = TripSerializer(many=True)
    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'trips'
        )
