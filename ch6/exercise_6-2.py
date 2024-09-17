#!/usr/bin/env python3

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]}) @{movie[2]}")
        print()

def add(movie_list):
    name = input("Name: ")
    year = int(input("Year: "))
    price = float(input("Price: "))  #added price to movie list item
    movie = [name, year, price]
    movie_list.append(movie)
    print(f"{movie[0]} was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie[0]} was deleted.\n")

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Find movies by year")   #added search option to menu
    print("exit - Exit program")
    print()

#add search function to find any movies equal to the year inputed and print out the results
def search(movie_list):
    count = 0
    searchTerm = input("Year: ")
    for i in range(len(movie_list)):
        if movie_list[i][1] == int(searchTerm):
            print(f"{movie_list[i][0]} was released in {movie_list[i][1]}")
            count +=1
        elif i == (len(movie_list)-1) and count == 0:
            print("Sorry! No results found for that year.")
    
    
def main():
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
                  ["On the Waterfront", 1954, 5.59],
                  ["Cat on a Hot Tin Roof", 1958, 7.95]]
    
    display_menu()
    
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "find":    #tied search function to menu choice
            search(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
