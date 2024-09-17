#!/usr/bin/env python3

# display a welcome message
print(f"The Area and Perimiter Program")
print()

# get input from the user
length= float(input("Enter the length:\t"))
width= float(input("Enter the width:\t"))

# calculate perimeter and area
perimeter = (length * 2) + (width *2)
area = length * width
            
# format and display the result
print()
print(f"Area:\t\t{area}")
print(f"Perimeter:\t{perimeter}")
print()
print(f"Bye!")


