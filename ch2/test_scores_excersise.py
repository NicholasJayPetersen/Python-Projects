#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
score1 =  int(input("Enter the score for test 1: "))
score2 = int(input("Enter the score for test 2: "))
score3 = int(input("Enter the score for test 3: "))

#calculate the total score
total_score = score1 + score2 + score3

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print(f"Your Scores:\t{score1}, {score2}, {score3}", sep=' | ')
print("Total Score:\t",total_score,
      "\nAverage Score:\t",average_score)
print()
print("Bye!")


