#!usr/bin/env python3

#Display the welcome message
print(f"The Test Scores Program")
print()
print(f"Enter 999 to end input")
print(f"====================")

#Create variables
counter =  0
score_total = 0

#loop tests scores to continue until finished
while True:
    test_score = int(input("Enter test score: "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    elif test_score == 999:
        break
    else:
        print(f"Test score must be from 0 through 100.",
              "Score discarded. Try again.")

#Calculate the average score
average_score = round(score_total/counter)

#Output the result
print(f"====================")
print(f"Total score: {score_total}"
      f"\nAverage Score: {average_score}")
print()
print(f"Bye!")
