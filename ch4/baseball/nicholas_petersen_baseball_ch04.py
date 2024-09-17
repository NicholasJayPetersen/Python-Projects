#!usr/bin/env python3

def display_separator():
    print("========================================================================")

def display_title():
    print("Baseball Team Manager\n" )

def display_menu():    
    print("MENU OPTIONS\n",
          "1 - Calculate batting Average\n",
          "2 - Exit Program")

def get_inputs():
    at_bat =int(input("Official number of at bats: "))      #get times at bat from the user
    hits = int(input("Number of hits: "))                           #get number of hits from the user
    return at_bat, hits                                                     #returns at _bat and hits to the main function variables
            
def get_batting_avg(at_bat, hits):                        
        average = round(float(hits/at_bat), 3)                      #calculate batting averge from given arguments
        return average                                                          #return the bating average to main function variable


def main ():
    display_separator()
    display_title()
    display_menu()
    display_separator()

    while True:
        menu = int(input("Menu option: "))    
        if menu == 1:
            print("Calculate batting average...")
            at_bat, hits = get_inputs()                             #calls funtion to prompt user to input times at bat and hits. then stores what is returned in variables
            average = get_batting_avg(at_bat, hits)      #gets the batting average based on at_bat and hits returned from the previous function
            print(f"Batting average: {average}\n")

        elif menu == 2:
            print("Bye!")
            break
        
        else:
            print("Not a valid option. Please try agian.\n")
            display_menu()
            display_separator()
        

if __name__ == "__main__":
    main()
