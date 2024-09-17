#!usr/bin/env python3

#display welcome message and description
print("========================================================================\n" +
        "\n" +
        "\t\tBaseball Team Manager\n" +
        "\n" +
        "This program calculates the batting average for a player based  on the player's official \n" +
        "number of at bats and hits. \n" +
        "\n" +
        "========================================================================")

#get the players name, times at bat, and number of hits
name = input("Player's Name:\t\t")
at_bat =int(input("Official number of at bats:\t"))
hits = int(input("Number of hits:\t\t"))

#calculate batting averge
average = round(float(hits/at_bat), 3)

#output bating average
print("\n" + name+"'s batting average is " + str(average))

#print an encouraging or discouraging message depending on the average
if average >= .33: print("Good Job " + name + " :)")
else:print (name + " sucks :(")

print("\nBye!")
