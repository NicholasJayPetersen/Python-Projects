#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user

    while (monthly_investment := float(input("Enter monthly investment:\t"))) <= 0:
        monthly_investment = float(input("Entry must be greater than 0. Try again: "))
        if monthly_investment > 0:
            break

    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    while True: 
        if yearly_interest_rate <= 0:
           yearly_interest_rate = float(input("Entry must be greater than 0. Try again: "))
           
        elif yearly_interest_rate > 15:
            yearly_interest_rate = float(input("Entry must be less than or equal to 15. Try again: "))

        else:
            break
            
    years = int(input("Enter number of years:\t"))
    while True: 
        if years < 0:
           years = int(input("Entry must be greater than 0 and less than or equal to 50. Try again: "))
           
        elif years > 50:
            years = int(input("Entry must be greater than 0 and less than or equal to 50. Try again: "))

        else:
            break
            
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(1, (months+1)):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        if (i%12) == 0: 
            print(f"Year = {int((i/12))}\t\t Future Value = {round(future_value, 2)}")


    # see if the user wants to continue
    print()
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
