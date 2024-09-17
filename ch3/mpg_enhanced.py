#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

#create loop to repeat the program
go_again = "y"
while go_again.lower() =="y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost = float(input("Enter the cost per gallon:    "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost <= 0:
        print("Cost must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)

        #calculate cost and diplay result
        cost_per_gallon = round(cost /gallons_used, 1)
        print("Cost Per Gallon:          ", cost_per_gallon)

    go_again = input(f"\nGet entries for another trip? (y/n): ")

    if go_again.lower() == "y":
        print()
        continue
    elif go_again.lower() == "n":
        print()
        break
    else:
        while go_again.lower() != "y" and go_again.lower() != "n":
            go_again = input("Your choice was invalid. Please enter 'y' for yes or 'n' for no: ")
            if go_again.lower() == "y" or go_again.lower() =="n":
                break

print()
print("Bye!")



