#! /usr/bin/env python3

#used to generate random number for die roll
import random

#calls other functions in the game where the die is either rolled or held to end the turn
def take_turn(turn, score, game_over):
    print("TURN ", turn)
    score_this_turn = 0
    turn_over = False
    while not turn_over:
        choice = input("Roll or hold? (r/h): ")
        if choice.lower()=="r":
            turn, score, score_this_turn, turn_over = roll_die(turn, score, score_this_turn)
        elif choice.lower()=="h":
            turn, score, turn_over, game_over = hold_turn(turn, score, score_this_turn)
        else:
            print("Invalid choice. Try again.")
    return turn, score, game_over

#simulates a die roll and adds to the score for that turn    
def roll_die(turn, score, score_this_turn):
    die = random.randint(1,6)
    print("Die: ", str(die))
    if die ==1:
        score_this_turn = 0
        turn += 1
        print ("Turn over. No score this turn.")
        turn_over = True
    else:
        score_this_turn += die
        turn_over = False
    return turn, score, score_this_turn, turn_over

#ends the turn and adds the score to the total
def hold_turn(turn, score, score_this_turn):
    print("Score for turn: ", score_this_turn)
    score += score_this_turn
    print("Total score: ", score, "\n")
    turn_over = True
    game_over = False
    if score >= 20:
        print("You finish in  ", turn, " turns.")
        game_over = True
        return turn, score, turn_over, game_over
    turn += 1
    return turn, score, turn_over, game_over

#prints out the title menu
def display_rules():
    print("Let's Play PIG!")
    print()
    print("See how many turns it takes you to get to 20.")
    print("Turn ends when you roll a 1.")
    print("If you roll a 1, you lose all points for that turn")
    print("If you hold, you will save all points for that turn")
    print()

#runs all functions to play the game
def play_game():
    turn = 1
    score = 0
    game_over = False
    while not game_over:
        turn, score, game_over = take_turn(turn, score, game_over)
    print()
    print("Game over!")

#launches the game
def main():
    display_rules()
    play_game()

#runs the main function first
if __name__ == "__main__":
    main()
