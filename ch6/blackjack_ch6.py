#!usr/bin/env python3

import random

def displayMenu():
    print(f"Blackjack Money Tracker!\nBlackjack payout is 3:2\nEnter 'x' to exit betting\n")

def getInputs():
    money = float(input("Starting money:\t"))
    bet = float(input("Bet amount:\t"))
    return money, bet

def validateInputs(money, bet):
    if money < 5 or money > 10000 or bet < 5 or bet > 1000:
        print("Starting money  must be between 5 and 10,000.\nBet amount must be between 5 and 1,000... Please try again.\n")
        isValid = False
        return isValid
    
    else:
        isValid = True
        return isValid

def validateBet(money, bet):
    if bet == "x":
        return bet

    while float(bet) <5 or float(bet) > 1000:
        bet = input("Please enter a bet between 5 and 1000: ")
        
    while float(bet) > money:
        bet = input("You dont have that much money! Please enter a lower number: ")
        if float(bet) <5 or float(bet) > 1000:
            bet = input("Please enter a bet between 5 and 1000: ")
    return bet


def playAgain():
    choice = input("Would you like to play again? (y/n): ")
    if choice.lower() == "n":
        print("Thanks for playing Blackjack. Bye!")
        bet = "x"
        return bet            
    elif choice.lower() == "y":
        main()
    
def playHand(money, bet):        
    while True:
        if str(bet).lower() == "x":
            break
        else:
            money = outcome(money, bet)
            if money > 0:
                print(f"You have ${money}")
                bet = (input("Bet amount:\t"))
            else:
                print(f"You lost your house!")
                bet = "x"

def outcome(money, bet):
    choice = random.randint(1,100)

    if choice > 0 and choice <= 5:
        blackjack = round(money + (float(bet)*(3/2)), 2)
        amount = round((float(bet)*(3/2)), 2)
        print(f"Blackjack!\nYou earned ${amount}.\n")
        return blackjack

    elif choice > 5 and choice <= 14:
        push = round(money, 2)
        print(f"Pushed...\nYou got your bet of ${bet} back and still have ${money} left.\n")
        return push
        
    elif choice > 14 and choice <= 51:
        win = round(money + float(bet), 2)
        print(f"Winner!\nYou earned ${bet}.\n")
        return win

    else:
        loss = round(money - float(bet), 2)
        print(f"Loss...\nYou lost ${bet}.\n")
        return loss

def main():
    displayMenu()

    suits =  [clubs, spades, diamonds, hearts]
    ranks = [[2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8], [9,9], ["Jack",10], ["Queen",10], ["King",10], ["Ace",1,10]]
    
    while True:
        money, bet = getInputs()
        isValid = validateInputs(money, bet)

        if isValid:
            break
        else:
            continue

    while True:
        if str(bet).lower() == "x":
            break
        else:
            money = outcome(money, bet)
            if money > 0:
                print(f"You have ${money}")
                bet = (input("Bet amount:\t"))
                bet = validateBet(money, bet)
            else:
                print(f"You lost your house!")
                bet = "x"
    playAgain()

if __name__ == "__main__":
    main()

