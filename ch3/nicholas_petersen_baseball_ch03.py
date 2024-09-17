#!usr/bin/env python3

#display welcome message and description
print("========================================================================\n",
        "Baseball Team Manager\n" ,
          "MENU OPTIONS\n",
          "1 - Calculate batting Average\n",
          "2 - Exit Program\n"
        "========================================================================")

#set variable for menu loop
menu = int(input("Menu option: "))

#set loop to offer menu option again after first iteration completes.
while True:

    #initailze menu selection loop
    if menu == 1:
        print("Calculate batting average...")

        #get times at bat, and number of hits
        at_bat =int(input("Official number of at bats: "))
        hits = int(input("Number of hits: "))

        #calculate batting averge
        average = round(float(hits/at_bat), 3)

        #output bating average
        print(f"Batting average: {average}\n")
        menu = int(input("Menu option: "))

    elif menu == 2:
        break

    else:
        menu = int(input("Not a valid option. Please try agian.\n\nMenu option: "))

print("Bye!")
