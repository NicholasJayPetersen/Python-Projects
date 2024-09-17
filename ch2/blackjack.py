#!usr/bin/env python3

#display the title and payout ratio
print(f"Blackjack Payout Calculator\nBlackjack payout is 3:2\n")

#get starting amount and bet from user
starting_money = float(input("Starting money:\t"))
bet = float(input("Bet amount:\t"))

#calculate blackjack/win/push/loss
blackjack = round(starting_money + (bet*(3/2)), 2)
win = round(starting_money + bet, 2)
push = round(starting_money, 2)
loss = round(starting_money - bet, 2)

#display the results in a table
print(f"\nENDING MONEY FOR ACCOUNT\n \
Blackjack:\t {blackjack}\n \
Win:\t\t {win}\n \
Push:\t\t {push}\n \
Loss:\t\t {loss}\n")

#exit the program
print("Bye!")
