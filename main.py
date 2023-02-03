from geopy.distance import geodesic
from geopy.geocoders import Nominatim

budget = 30000
number_of_people = 3
num_days = 3
city1 = 'Mumbai'
geolocator = Nominatim(user_agent="user")
location1 = geolocator.geocode(city1)
city1_lat = (location1.latitude, location1.longitude)
city2 = 'Jaipur'
geolocator = Nominatim(user_agent="user1")
location2 = geolocator.geocode(city2)
city2_lat = (location2.latitude, location2.longitude)
distance = geodesic(city1_lat, city2_lat).km
cost_of_train_per_km_india = 1.41
cost_per_user_train = cost_of_train_per_km_india * distance
avg_cheap_hotel_per_person_india = 850
avg_mid_hotel_per_person_india = 1700
avg_expensive_hotel_per_person_india = 3000
hotel_price_final_per_use = avg_cheap_hotel_per_person_india
avg_use_cost = (budget / (num_days * number_of_people))
if 0 < avg_use_cost < 5000:
    hotel_price_final_per_use = avg_cheap_hotel_per_person_india
elif 5000 < avg_use_cost < 10000:
    hotel_price_final_per_use = avg_mid_hotel_per_person_india
else:
    hotel_price_final_per_use = avg_expensive_hotel_per_person_india

avg_food_cost_per_day_per_user = 800

total_price = (((avg_food_cost_per_day_per_user + hotel_price_final_per_use) * num_days) + cost_per_user_train * 2) * number_of_people
value = round(budget - total_price)
print(value)
flight_price_per_person = 4.25 * distance
total_price_in_flight = (((avg_food_cost_per_day_per_user + hotel_price_final_per_use) * num_days) + flight_price_per_person * 2) * number_of_people
new_value = budget - total_price_in_flight

if value < (budget * 0.1):
    print("Not feasible")
elif (budget * 0.1) < value < (budget * 0.2):
    print("feasible and use train")
elif value > (budget * 0.22) and new_value > (0.08 * budget):
    print(" feasible and switch to flight")
else:
    print("feasible")



