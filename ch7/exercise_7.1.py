#!/usr/bin/env python3

import csv
FILENAME = "trips.csv"

def write_mpg(mpg_list):
    with open(FILENAME, "w", newline="") as file:
        new_list= csv.writer(file)
        new_list.writerows(mpg_list)

def read_mpg():
    mpg_list = []
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            mpg_list.append(row)
    return mpg_list

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()                        
        mpg = round((miles_driven / gallons_used), 2)

        mpg_list = read_mpg()
        if len(mpg_list) == 0:
            mpg_list.append(["Distance", "Gallons", "MPG"])
            mpg_list.append([miles_driven, gallons_used, mpg])
        else:
            mpg_list.append([miles_driven, gallons_used, mpg])
            
        write_mpg(mpg_list)
        
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        for i in range(len(mpg_list)):
            print(f"{mpg_list[i][0]}\t{mpg_list[i][1]}\t{mpg_list[i][2]}")
        print()
            
        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()

