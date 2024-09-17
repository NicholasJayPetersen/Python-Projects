#!usr/bin/env python3

import random

def displayMenu():
    print(f"Blackjack Money Tracker!\nBlackjack payout is 3:2\nEnter 'x' to exit betting\n")

def quitGame():
    print("Thanks for playing Blackjack. Bye!")

def getInputs():
    money = float(input("Starting money:\t"))
    bet = (input("Bet amount:\t"))
    return money, bet

def getNextBet():
    bet = (input("Bet amount:\t"))
    return bet

def playAgain():
    choice = input("Would you like to play again? (y/n): ")
    if choice.lower() == "n":
        bet = "x"
        return bet            
    elif choice.lower() == "y":
        playHand()
    
def playHand():
    money, bet = getInputs()
    while True:
        if str(bet).lower() == "x":
            break
        else:
            money = outcome(money, bet)
            if money > 0:
                print(f"You have ${money}")
                bet = getNextBet()
            else:
                print(f"You lost your house!")
                bet = "x"
    playAgain()

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
    playHand()
    quitGame()

if __name__ == "__main__":
    main()

