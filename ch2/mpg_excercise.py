#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter the cost per gallon\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)

# calculate total gas cost for the trip
total_cost = round(miles_driven / cost_per_gallon, 1)

#calculate cost per mile
cost_per_mile = round(total_cost / miles_driven, 1)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t{mpg}")
print(f"Total Gas Cost:\t\t${total_cost}")
print(f"Cost Per Mile:\t\t${cost_per_mile}")
print()
print("Bye!")


