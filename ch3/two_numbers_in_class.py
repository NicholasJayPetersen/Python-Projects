#!usr/bin/env python3

#The two numbers program

#Print opening message
print(f"This program will take two whole numbers and tell you which one is larger!")

#Get numbers from the user
num1 = int(input("please enter your first number: "))
num2 = int(input("please enter your second number: "))
print()

#Compare if the first number is larger, if so print that is is.
if num1 > num2:
    print(num1, "is greater than", num2)

#If not, print the other number is larger
else:
    print(num2, "is greater than", num1)

print(f"\nThanks for comparing your numbers. Bye!")
