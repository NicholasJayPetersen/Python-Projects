#! /usr/bin/env python3

import random

#creates data statistics for a given list or tuple of numbers
def crunch_numbers(data):
    total = 0
    for number in data:  #runs through each index of the list adding the values to find the sum
        total += number

    average = round(total / len(data)) #divides the sum of all numbers by the list length
    median_index = len(data) // 2 #integer division finds the middle of the list/tuple
    median = data[median_index]  #pulls the number found in the last line
    minimum = min(data) #finds the smallest number
    maximum = max(data) #finds the largest number
    dups = get_duplicates(data) #pulls the duplicates found in the next function

    print("Average = ", average,
          "Median = ", median,
          "Min = ", minimum,
          "Max = ", maximum,
          "Dups = ", dups)

#detects any duplicate numbers in the list or tuple
def get_duplicates(data):
    dups = []

    #for each item in the list, count function looks for other occurences of that item and stores it
    for i in range(51): 
        count = data.count(i)
        if count >= 2:
            dups.append(i)
    return dups

def main():
    fixed_tuple= (0,5,10,15,20,25,30,35,40,45,50) #immutable list
    random_list = [0] * 11 #creates a list of 11 integers all valued at 0

    #random function fills the list of 0s with random numbers
    for i in range(len(random_list)):
        random_list[i] = random.randint(0,50)
    random_list.sort()

    print("Tuple Data: ", fixed_tuple)
    crunch_numbers(fixed_tuple)
    print()
    print("Random Data: ", random_list)
    crunch_numbers(random_list)

if __name__ == "__main__":
    main()
