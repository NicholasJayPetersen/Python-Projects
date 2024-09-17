#! usr/bin/env python3

POSITIONS = ("1B", "2B", "3B", "P", "C", "SS", "LF", "CF", "RF")

def display_separator():
    print("========================================================================")

def display_title():
    print("Baseball Team Manager\n" )

def display_menu(positions):
    print("MENU OPTIONS\n",
          "1 - Display Lineup\n",
          "2 - Add Player\n",
          "3 - Remove Player\n",
          "4 - Move Player\n",
          "5 - Edit Player Position\n",
          "6 - Edit Player Stats\n",
          "7 - Exit Program\n")
    print()
    print("POSITIONS")
    print(*POSITIONS, sep=" | ")

def get_inputs():
    at_bat =int(input("Official number of at bats: "))             #NOT USED in this version
    hits = int(input("Number of hits: "))                                  #NOT USED in this version
    return at_bat, hits

def get_batting_avg(at_bat, hits):                        
        average = round(float(hits/at_bat), 3)                           #NOT USED in this version
        return average                                                                #NOT USED in this version

def validate_avg(at_bat, hits):
    while at_bat <= 0:                                                               #check to ensure numbers are not negative
        print("You cannot have less than one time at bat. Please try again...\n")
        at_bat =int(input("Official number of at bats: "))          #get times at bat from the user while negative
        
    while hits < 0:
        print("You cannot have less than zero hits. Please try again...\n")
        hits =int(input("Number of hits: "))                                  #get number of hits from the user while negative
    
    if at_bat >= hits and at_bat >=0 and hits >=0:
        return at_bat, hits                                                             #returns at _bat and hits to the main function variables if passes validation
        
    else:                                                                                      #validation failed since hits was greater than at_bat. Get new inputs from the user
        while at_bat < hits:                                                           # check again to ensure numbers are not negative after reentry
            print("Your entry was invalid. Times at bat must be greater than or equal to hits. Please try again...\n")
            at_bat =int(input("Official number of at bats: "))         #get times at bat from the user
            hits = int(input("Number of hits: "))                              #get number of hits from the user
            
            while at_bat < 0:                                                            # check again to ensure numbers are not negative after reentry
                print("You cannot have less than zero times at bat. Please try again...\n")
                at_bat =int(input("Official number of at bats: "))      #get times at bat from the user
        
            while hits < 0:
                print("You cannot have less than zero hits. Please try again...\n")
                hits =int(input("Number of hits: "))                            #get number of hits from the user
                
        return at_bat, hits

def validate_pos(position):
    while True:
       validatePos = POSITIONS.count(position)
       if validatePos == 0:
           position = input("Position not valid. Please choose from the list above: ")
       else:
            break
    return position

def showLineup(list_data):
    print("LINEUP")
    print("   Player\t\t\tPosition\tAt bats\tHits\tAverage")
    print("-------------------------------------------------------------------------------------------------------------------")
    for i, list_data in enumerate(list_data, start=1):
        if len(list_data[0]) > 25:                                                  #check name length and truncate if too long to fit in column
            print(f"{i}. {list_data[0][0:22]}...\t{list_data[1]}\t{list_data[2]}\t{list_data[3]}\t{list_data[4]}")
        else:                                                                                 #otherwise print full name up to 20 characters
            print(f"{i}. {list_data[0].ljust(25, " ")}\t{list_data[1]}\t{list_data[2]}\t{list_data[3]}\t{list_data[4]}")
    print()

def addPlayer(list_data):
    name = input("Enter player name: ")
    position = input("Enter their position: ")
    position = validate_pos(position)
    at_bat =int(input("Official number of at bats: "))                 #get times at bat from the user
    hits = int(input("Number of hits: "))                                       #get number of hits from the user
    at_bat, hits = validate_avg(at_bat, hits)
    average = round(float(hits/at_bat), 3)
    if average == 0:
        average = "<0.001"
    print(f"{name} was added to the team.")
    print()
    list_data.append([name, position, at_bat, hits, average])

def removePlayer(list_data):
    delete = input("which player number would you like to remove?: ")
    print(f"{list_data[int(delete)-1][0]} has been removed from the team")
    print()
    list_data.pop(int(delete) -1)

def movePlayer(list_data):
    currentNum = input("Current lineup number: ")
    newNum = input("New lineup number: ")
    placeholder = list_data.pop(int(currentNum) - 1)
    list_data.insert((int(newNum)-1), placeholder)
    print(f"{list_data[int(newNum)-1][0]} was moved to position {newNum} in the lineup.")
    print()

def changePosition(list_data):
    print("POSITIONS")
    print(*POSITIONS, sep=" | ")
    player = input("Current lineup number: ")
    newPos = input("Enter the new position: ")
    newPos = validate_pos(newPos)
    currentPos=  list_data[int(player)-1][1]
    list_data[int(player)-1][1] = newPos
    print(f"{list_data[int(player)-1][0]}'s position was changed from {currentPos} to {newPos}.")
    print()

def changeStats(list_data):
    player = input("Current lineup number: ")
    at_bat =int(input("Official number of at bats: "))                  #get times at bat from the user
    hits = int(input("Number of hits: "))                                       #get number of hits from the user
    at_bat, hits = validate_avg(at_bat, hits)
    average = round(float(hits/at_bat), 3)
    if average == 0:
        average = "<0.001"
    list_data[int(player)-1][2] = at_bat
    list_data[int(player)-1][3] = hits
    list_data[int(player)-1][4] = average
    print(f"Stats for {list_data[int(player)-1][0]} have been updated.")
    print()

def main ():
    players = [["Javier Baez", "SS", "510", "113", "0.222"],["Colt Kieth", "3B", "507", "155", "0.036"],["Kenta Maeda", "P", "48", "12","0.250"],["Spencer Torkelson", "1B", "606", "141", "0.233"],["Name Too Long To Fit In The Column So Its Truncated", "SS", "1000", "1000", "1.000"]]

    display_separator()
    display_title()
    display_menu(POSITIONS)
    display_separator()

    while True:
        menu = (input("Menu option: "))
        if menu == "1":
            showLineup(players)
        elif menu == "2":
             addPlayer(players)
        elif menu == "3":
            removePlayer(players)
        elif menu == "4":
            movePlayer(players)
        elif menu == "5":
            changePosition(players)
        elif menu == "6":
            changeStats(players)
        elif menu == "7":
            print("Bye!")
            break                
        else:
            print("Not a valid option. Please try agian.\n")
            display_menu(POSITIONS)
            display_separator()
        

if __name__ == "__main__":
    main()
