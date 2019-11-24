# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import json
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework import status
from trips.models import Country
from trips.models import City
from trips.models import Trip
from trips.serializers import CitySerializer
from trips.serializers import CountrySerializer
from trips.serializers import TripSerializer
from trips.serializers import TripByCitySerializer
from django.views import View
from rest_framework.response import Response
from django.core.exceptions import ValidationError


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class get_trips_by_city(generics.ListAPIView):

    queryset = City.objects.all()
    serializer_class = TripByCitySerializer

    def list(self, request, city_uuid):
        try:
            city = City.objects.get(pk=city_uuid)
        except ValidationError as e:
            return Response({'status':'err', 'message': e}, status=status.HTTP_400_BAD_REQUEST)
        except City.DoesNotExist as e:
            return Response({'status':'err', 'message': 'City matching query does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TripByCitySerializer(city)
        json_serializers = json.loads(JSONRenderer().render(serializer.data))

        return Response(json_serializers, status=status.HTTP_200_OK)

