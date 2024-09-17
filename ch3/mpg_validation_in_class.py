#!usr/bin/env python3

# display a welcome message
print(f"The Miles Per Gallon Program")
print()

# get input from the user
miles_driven = float(input(f"Enter miles driven:\t\t")) #get miles driven
gallons_used = float(input(f"Enter gallons of gas used:\t")) #get gallons used


#data validation for user data entered
if miles_driven <= 0:
    print(f"Miles driven must be greater than zero. Please try again.") #miles cannot be zero
elif gallons_used <= 0:
    print(f"Gallons used must be greater than zero. Please try again.") #gallons used cannot be zero
else:
    # calculate and display miles per gallon
    mpg = round((miles_driven / gallons_used), 2)
    print(f"Miles Per Gallon:\t\t{mpg}")

print()
print(f"Bye!")
