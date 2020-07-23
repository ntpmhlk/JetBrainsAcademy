# put your python code here
days = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())
print((food_cost * days) + (hotel_cost * (days - 1)) + (flight_cost * 2))
