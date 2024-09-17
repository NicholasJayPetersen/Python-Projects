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
    return at_bat, hits


def validate_inputs(at_bat, hits):
    while at_bat <= 0:                                                           #check to ensure numbers are not negative
        print("You cannot have less than one time at bat. Please try again...\n")
        at_bat =int(input("Official number of at bats: "))      #get times at bat from the user while negative
        
    while hits < 0:
        print("You cannot have less than zero hits. Please try again...\n")
        hits =int(input("Number of hits: "))                            #get number of hits from the user while negative
    
    if at_bat >= hits and at_bat >=0 and hits >=0:
        return at_bat, hits                                                     #returns at _bat and hits to the main function variables if passes validation
        
    else:                                                                               #validation failed. Get new inputs from the user
        while at_bat < hits:                                                    # check again to ensure numbers are not negative after reentry
            print("Your entry was invalid. Times at bat must be greater than or equal to hits. Please try again...\n")
            at_bat =int(input("Official number of at bats: "))      #get times at bat from the user
            hits = int(input("Number of hits: "))                           #get number of hits from the user
            
            while at_bat < 0:                                                       # check again to ensure numbers are not negative after reentry
                print("You cannot have less than zero times at bat. Please try again...\n")
                at_bat =int(input("Official number of at bats: "))      #get times at bat from the user
        
            while hits < 0:
                print("You cannot have less than zero hits. Please try again...\n")
                hits =int(input("Number of hits: "))                            #get number of hits from the user
                
        return at_bat, hits
            
            
def get_batting_avg(at_bat, hits):                        
        average = round(float(hits/at_bat), 3)                      #calculate batting averge from given arguments
        return average                                                          #return the bating average to main function variable


def main ():
    display_separator()
    display_title()
    display_menu()
    display_separator()

    while True:
        menu = (input("Menu option: "))    
        if menu == "1":
            print("Calculate batting average...")
            at_bat, hits = get_inputs()                                  #calls funtion to prompt user to input times at bat and hits. then stores what is returned in variables
            at_bat, hits = validate_inputs(at_bat, hits)        #checks inputs to ensure hits does not exceed times at bat and are positive numbers.
            average = get_batting_avg(at_bat, hits)            #gets the batting average based on at_bat and hits returned from the previous function
            if average == 0:                                                    # If number is too small and rounds to 0, notify user its less than .001. 
                print("Average is less than 0.001")
            else:
                print(f"Batting average: {average}\n")

        elif menu == "2":
            print("Bye!")
            break
        
        else:
            print("Not a valid option. Please try agian.\n")
            display_menu()
            display_separator()
        

if __name__ == "__main__":
    main()
