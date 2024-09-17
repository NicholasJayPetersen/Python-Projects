#!/usr/bin/env python3
import csv
FILENAME = "trips.csv"

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def write_trips(trips):
    with open(FILENAME, "w", newline="") as file:
        new_list= csv.writer(file)
        new_list.writerows(trips)
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = []
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()              
        mpg = round((miles_driven / gallons_used), 2)
        trips.append([miles_driven, gallons_used, mpg])

        print(f"Miles Per Gallon:\t{mpg}")
        print()
        print("Distance\tGallons\tMPG")
        for i in range(len(trips)):
            print(f"{trips[i][0]}\t{trips[i][1]}\t{trips[i][2]}")
        
        more = input("More entries? (y or n): ")

    write_trips(trips)
    print("Bye!")

if __name__ == "__main__":
    main()

