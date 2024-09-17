#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'end' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

#set loop to promp user to continue after test score entry
go_again = "y"
while True:
    if go_again.lower() =="n":
        break
    elif go_again.lower() != "y":
        go_again = input("Your choice was invalid. Please enter 'y' for yes or 'n' for no: ")

    
    #loop test score entry | Comment out original loop
#    while test_score != 999:
#        test_score = (input("Enter test score: "))
#        if test_score.lower() == "end":
#            break

#        elif int(test_score) >= 0 and int(test_score) <= 100:
#            score_total += int(test_score)
#            counter += 1
        
#        else:
#            print(f"Test score must be from 0 through 100. "
#                    f"Score discarded. Try again.")
#   else:
#           print("Your choice was invalid. Please enter 'y' for yes or 'n' for no: ")


    #loop test score entry
    while (test_score := input("Enter test score: ").lower()) != "end":
        if int(test_score) >= 0 and int(test_score) <= 100:
            score_total += int(test_score)
            counter += 1
        
        else:
            print(f"Test score must be from 0 through 100. "
                    f"Score discarded. Try again.")

                
    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
        f"\nAverage Score: {average_score}")

    #check if user wants to contine and validate the entry
    test_score = 0
    go_again = input("\nEnter another set of test scores (y/n)? ")
    print()
    while go_again.lower() != "y" and go_again.lower() != "n":
        go_again = input("Your choice was invalid. Please enter 'y' for yes or 'n' for no: ")
        if go_again.lower() == "y" or go_again.lower() == "n":
            break

print()
print("Bye!")


