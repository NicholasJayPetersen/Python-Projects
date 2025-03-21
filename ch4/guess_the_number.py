#! /usr/bin/env python3

import random

LIMIT=10

def display_title():
    print("Guess the number!")
    print()

def play_game():
    number = random.randint(1, LIMIT)
    print(f"I'm thinking of a number between 1 and {LIMIT}.\n")
    count = 1
    while (guess := int(input("Your Guess: "))) != number:
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count +=1
    print(f"You guessed it in {count} tries!\n")

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again? (y/n): ")
        while again.lower() != "y" and again.lower() != "n":
            again = input('Please choose either "y" or "n": ')

    print("Bye!")

if __name__ == "__main__":
    main()
