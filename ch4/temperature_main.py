#! /usr/bin/env python3

#import temp functions
import temperature as temp

#function to display the main menu
def display_menu():
    print("MENU")
    print("1. Fahrenheit to Celcius")
    print("2. Celcius to Fahrenheit")
    print()

#function to convert temp by calling functions in another file
def convert_temp():
    option = int(input("Enter an option menu: "))
    while option != 1 and option != 2:
        option = int(input("You must enter a valid number. Choose 1 or 2: "))
            
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c = temp.to_celcius(f)
        c = round(c, 2)
        print("Degrees Celcius: ", c)

    elif option == 2:
        c = int(input("Enter degrees Celcius: "))
        f = temp.to_fahrenheit(c)
        f = round(f, 2)
        print("Degrees Fahrenheit: ", f)

#run program using prebuilt functions
def main():
    display_menu()
    again = "y"
    while again.lower()=="y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y/n): ")
        while again.lower() != "y" and again.lower() != "n":
            again = input("please enter a valid menu choice: ")

    print("Bye!")

#run main function first
if __name__ == "__main__":
    main()
