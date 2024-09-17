#!/usr/bin/env python3

# display a welcome message
print("The Most Accurate Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
total_score += int(input("Enter test score: ")) #add the first test score to the variable and store it.
total_score += int(input("Enter test score: ")) #add the second test score to the variable and store it.
total_score += int(input("Enter test score: ")) #add the third test score the variable and store it.

# calculate average score
average_score = round(total_score / 3) #take the combined scores and divide by how many tests there are
             
# format and display the result
print("======================")
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Isnt this program the best, Nicholas Petersen?... Bye!")


