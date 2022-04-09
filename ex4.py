# number of cars available
cars = 100

# space available in each individual car
space_in_a_car = 4.0

# number of drivers available
drivers = 30

# number of passengers
passengers = 90

# number of cars without available drivers
cars_not_driven = cars - drivers

# number of cars driven is equal to the number of available drivers
cars_driven = drivers

# carpool capacity is total cars driven multiplied by the space available in each car
carpool_capacity = cars_driven * space_in_a_car

# average passengers in each car is the total number of passengers divided by the number of cars driven
avearage_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", avearage_passengers_per_car, "in each car.")
