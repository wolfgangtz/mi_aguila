"""mi_aguila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view
from trips.views import CountryList
from trips.views import CountryDetail
from trips.views import CityList
from trips.views import CityDetail
from trips.views import TripList
from trips.views import TripDetail
from trips.views import get_trips_by_city


schema_view = get_swagger_view(title='Mi Aguila API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^swagger/', schema_view),

    # City Endpoint's
    path(
        'city/',
        CityList.as_view(),
        name='City list'
    ),
    re_path(
        '^city/(?P<pk>[0-9a-f-]+)/$',
        CityDetail.as_view(),
        name='City detail'
    ),


    # Country Endpoint's
    path(
        'country/',
        CountryList.as_view(),
        name='Country list'
    ),
    re_path(
        '^country/(?P<pk>[0-9a-f-]+)/$',
        CountryDetail.as_view(),
        name='Country detail'
    ),


    # Trip Endpoint's
    path(
        'trip/',
        TripList.as_view(),
        name='Trip list'
    ),
    re_path(
        '^trip/(?P<pk>[0-9a-f-]+)/$',
        TripDetail.as_view(),
        name='Trip detail'
    ),
    re_path(
        'trip/city/(?P<city_uuid>[0-9a-f-]+)/$',
        get_trips_by_city.as_view(),
        name='Get trip\'s by city.'
    ),
]
