#!usr/bin/env python3

#display the title and payout ratio
print(f"Blackjack Money Tracker!\nBlackjack payout is 3:2\nEnter 'x' to exit betting\n")

#get starting amount and bet from user
money = float(input("Starting money:\t"))

#set continuous loop until user enters 'x' to exit
while True:
    bet = (input("Bet amount:\t"))
    if str(bet).lower() == "x":
        break
    
    choice = str(input("Blackjack, win, push, or lose? (b/w/p/l): "))

    #determine output based on users choice
    if choice.lower() == "b":
        blackjack = round(money + (float(bet)*(3/2)), 2)
        money = blackjack
        print(f"Money: {money}\n\nEnter another bet?")

    elif choice.lower() =="w":
        win = round(money + float(bet), 2)
        money = win
        print(f"Money: {money}\n\nEnter another bet?")
        
    elif choice.lower() == "p":
        push = round(money, 2)
        money = push
        print(f"Money: {money}\n\nEnter another bet?")

    elif choice.lower() == "l":
        loss = round(money - float(bet), 2)
        money = loss
        print(f"Money: {money}\n\nEnter another bet?")

    else:
        print(f"The choice you enterd is invalid. Please try again using one of the allowed letters.")

#exit the program
print("\nThanks for using me to keep track of your money. Bye!")
