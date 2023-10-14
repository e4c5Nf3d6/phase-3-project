# lib/cli.py

from helpers import (
    exit_program,
    list_artists,
    list_paintings,
    list_movements
)

def main():
    m = "main"
    while m == "main":
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            artists()
        elif choice == "2":
            paintings()
        elif choice == "3":
            movements()
        else:
            print("Invalid choice")

def artists():
    m = "artists"
    while m == "artists":
        artists_menu()
        choice = input("> ")
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_artists()
        elif choice == "2":
            pass
        else:
            print("Invalid choice")

def paintings():
    m = "paintings"
    while m == "paintings":
        paintings_menu()
        choice = input("> ")
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_paintings()
        elif choice == "2":
            pass
        else:
            print("Invalid choice")

def movements():
    m = "movements"
    while m == "movements":
        movements_menu()
        choice = input("> ")
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_movements()
        elif choice == "2":
            pass
        else:
            print("Invalid choice")

def main_menu():
    print("Main Menu")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Artists")
    print("2. Paintings")
    print("3. Movements")

def artists_menu():
    print("Artist Menu")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. List all artists")
    print("2. Find artist by name")
    print("3. Find artist by id")
    print("4: Create artist")
    print("5: Update artist")
    print("6: Delete artist")

def paintings_menu():
    print("Paintings Menu")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. List all paintings")
    print("2. Find painting by name")
    print("3. Find painting by id")
    print("4: Create painting")
    print("5: Update painting")
    print("6: Delete painting")

def movements_menu():
    print("Movements Menu")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. List all movements")
    print("2. Find movement by name")
    print("3. Find movement by id")
    print("4: Create movement")
    print("5: Update movement")
    print("6: Delete movement")

if __name__ == "__main__":
    main()
