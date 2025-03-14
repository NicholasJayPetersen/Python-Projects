#! /usr/bin/env python3

#set a function to calculate the future value when called
def calculate_future_value (monthly_investment, yearly_interest, years):
    #convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    #calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value

def main():
    choice = "y"
    while choice.lower()=="y":
        #get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        yearly_interest_rate = float(input("Enter yearly interest rate investment:\t"))
        years = int(input("Enter the number of years:\t\t"))

        #call function and display future value
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()
    print("bye")

#run main function first
if __name__=="__main__":
    main()
