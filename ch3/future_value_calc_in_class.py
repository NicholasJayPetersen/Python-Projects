#!/usr/bin/env python3

#Display welcome message
print(f"Welcome to the Future Value Calculator")
print()

#initialize loop and set condition to lower case
choice = "y"
while choice.lower() == "y":
    #get investment amounts from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter annual interest rate:\t"))
    years = int(input("Enter the number of years:\t"))

    #convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate/12/100
    months = years * 12

    #calculate future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    #output the results
    print(f"Future value:\t\t{round(future_value,2)}")

    #continue?
    choice = input("continue? (y/n): ")

#say goodbye
print(f"Thanks for using the future value calculator. Bye!")
