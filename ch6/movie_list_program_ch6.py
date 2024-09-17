#! /usr/bin/env python3

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def list_movies(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie}")
    print()

def add_movie(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")

def delete_movie(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number. \n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted. \n")

def main():
    movie_list = ["Star Wars: Episode 3 - Revenge of the Sith", "Deadpool", "Lord of the Rings: The Two Towers", "The Revenant", "Oppenheimer"]

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movie_list)
        elif command.lower() == "add":
            add_movie(movie_list)
        elif command.lower() == "del":
            delete_movie(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print ("Not a valid command. Please try again. \n")
    print("Bye!")

if __name__ == "__main__":
    main()
    
