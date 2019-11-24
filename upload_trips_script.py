from trips.models import Country
from trips.models import City
from trips.models import Trip
import json

#Read trips from .json file
with open('trips.json') as trips:
     data = json.load(trips)
     for trip in data['trips']:
         #validate if city exist
         try:
             city = City.objects.get(name=trip["city"]["name"])
         except City.DoesNotExist as e:
             #City does not exist, we will create the city
             city = City(name=trip["city"]["name"])
             city.save()
         #validate if country exist
         try:
             country = Country.objects.get(name=trip["country"]["name"])
         except Country.DoesNotExist as e:
             #Country does not exist, we will create the Country
             country = Country(name=trip["country"]["name"])
             country.save()
         #Get trip info
         try:
             status = trip["status"] 
         except:
             status  = None
         try:
             price = trip["price"] 
         except:
             price  = None
         try:
             start_date = trip["start"]["date"]["$date"] 
         except:
             start_date  = None
         try:
             end_date = trip["end"]["date"]["$date"] 
         except:
             end_date  = None
         try:
             start_pickup_address = trip["start"]["pickup_address"] 
         except:
             start_pickup_address  = None
         try:
             start_pickup_location_type = trip["start"]["pickup_location"]["type"] 
         except:
             start_pickup_location_type  = None
         try:
             start_pickup_location_latitude = trip["start"]["pickup_location"]["coordinates"][0] 
         except:
             start_pickup_location_latitude  = None
         try:
             start_pickup_location_longitude = trip["start"]["pickup_location"]["coordinates"][1] 
         except:
             start_pickup_location_longitude  = None
         try:
             end_pickup_address = trip["end"]["pickup_address"] 
         except:
             end_pickup_address  = None
         try:
             end_pickup_location_type = trip["end"]["pickup_location"]["type"] 
         except:
             end_pickup_location_type  = None
         try:
             end_pickup_location_latitude = trip["end"]["pickup_location"]["coordinates"][0] 
         except:
             end_pickup_location_latitude  = None
         try:
             end_pickup_location_longitude = trip["end"]["pickup_location"]["coordinates"][1] 
         except:
             end_pickup_location_longitude  = None
         try:
             passenger_first_name = trip["passenger"]["first_name"] 
         except:
             passenger_first_name  = None
         try:
             passenger_last_name = trip["passenger"]["last_name"] 
         except:
             passenger_last_name  = None
         try:
             driver_first_name = trip["driver"]["first_name"] 
         except:
             driver_first_name  = None
         try:
             driver_last_name = trip["driver"]["last_name"] 
         except:
             driver_last_name  = None
         try:
             driver_location_type = trip["driver_location"]["type"] 
         except:
             driver_location_type  = None
         try:
             driver_location_latitude = trip["driver_location"]["coordinates"][0] 
         except:
             driver_location_latitude  = None
         try:
             driver_location_longitude = trip["driver_location"]["coordinates"][1] 
         except:
             driver_location_longitude  = None
         try:
             car_plate = trip["car"]["plate"] 
         except:
             car_plate  = None
         try:
             check_code = trip["check_code"] 
         except:
             check_code  = None
         #Create trip
         trip = Trip(
             status = status,
             price = price,
             start_date = start_date,
             end_date = end_date,
             start_pickup_address = start_pickup_address,
             start_pickup_location_type = start_pickup_location_type,
             start_pickup_location_latitude = start_pickup_location_latitude,
             start_pickup_location_longitude = start_pickup_location_longitude,
             end_pickup_address = end_pickup_address,
             end_pickup_location_type = end_pickup_location_type,
             end_pickup_location_latitude = end_pickup_location_latitude,
             end_pickup_location_longitude = end_pickup_location_longitude,
             passenger_first_name = passenger_first_name,
             passenger_last_name = passenger_last_name,
             driver_first_name = driver_first_name,
             driver_last_name = driver_last_name,
             driver_location_type = driver_location_type,
             driver_location_latitude = driver_location_latitude,
             driver_location_longitude = driver_location_longitude,
             car_plate = car_plate,
             check_code = check_code,
             city = city,
             country = country
         )
         trip.save()