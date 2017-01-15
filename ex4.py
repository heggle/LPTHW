#This exercise is for variables and names

#create an integer variable 
cars = 100
drivers = 30
passengers = 90

#create a float variable called "space in car"
	#(what would this even be? Occupants as a float??)
space_in_a_car = 4.0

#create variables using other variables or math
cars_not_driven = cars - drivers #integer
cars_driven = drivers #integer
carpool_capacity = cars_driven*space_in_a_car #float
average_passengers_per_car = passengers/cars_driven #integer

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We to need to put about", average_passengers_per_car, "in each car."



