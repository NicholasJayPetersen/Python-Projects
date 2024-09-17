#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []   #changed test scores variable to list
    while True:
        user_input = input("Enter test score: ")
        if user_input == "x":
            return  scores

        #modified validation check to work with the list
        else:
            user_input = int(user_input)
            scores.append(user_input)
            if scores[len(scores)-1] < 0 or scores[len(scores)-1] > 100:
                scores.pop(len(scores)-1)
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")
            else:
                continue


def process_scores(scores):
    # calculate average score
    total = 0
    for i in  range(len(scores)):
        total += scores[i]
    average = round(total / len(scores),2)   #modified average formula to use the list
                
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Lowest Score:   ", min(scores))
    print("Highest Score:   ", max(scores))
    print("Median Score:   ", scores[int(len(scores)) // 2])

def main():
    display_welcome()
    scores = get_scores()  #function returns list of scores to the variable in main
    process_scores(scores) #f passes the scores list to the function for processing
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


