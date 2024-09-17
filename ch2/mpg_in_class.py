#!/usr/bin/env python3

# display a welcome message
print("The Super Duper Miles Per Gallon Program!!")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))               #stores miles driven
gallons_used = float(input("Enter gallons of gas used:\t"))     #stores gallons of gas used

# calculate and round miles per gallon
mpg = miles_driven / gallons_used           #calculate miles per gallon and stores it
mpg = round(mpg, 2)                                 #rounds miles per gallon to the nearest hundredth

# display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print()
print("Thanks for using this super duper app, Nicholas Petersen. Bye!")


