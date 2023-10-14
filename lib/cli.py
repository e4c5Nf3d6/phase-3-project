# lib/cli.py

import click

from helpers import (
    exit_program,
    list_artists,
    find_artist_by_name,
    find_artist_by_id,
    create_artist,
    update_artist, 
    delete_artist,
    list_paintings,
    find_painting_by_name,
    find_painting_by_id,
    create_painting,
    update_painting,
    delete_painting,
    list_movements,
    find_movement_by_name,
    find_movement_by_id,
    create_movement,
    update_movement,
    delete_movement,
    list_artists_by_movement,
    list_paintings_by_artist,
    list_paintings_by_movement
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
            click.secho('Invalid choice', fg='red')

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
            find_artist_by_name()
        elif choice == "3":
            find_artist_by_id()
        elif choice == "4":
            create_artist()
        elif choice == "5":
            update_artist()
        elif choice == "6":
            delete_artist()
        elif choice == "7":
            list_artists_by_movement()
        else:
            click.secho('Invalid choice', fg='red')

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
            find_painting_by_name()
        elif choice == "3":
            find_painting_by_id()
        elif choice == "4":
            create_painting()
        elif choice == "5":
            update_painting()
        elif choice == "6":
            delete_painting()
        elif choice == "7":
            list_paintings_by_artist()
        elif choice == "8":
            list_paintings_by_movement()
        else:
            click.secho('Invalid choice', fg='red')

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
            find_movement_by_name()
        elif choice == "3":
            find_movement_by_id()
        elif choice == "4":
            create_movement()
        elif choice == "5":
            update_movement()
        elif choice == "6":
            delete_movement()
        else:
            click.secho('Invalid choice', fg='red')

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
    print("7: List artists by movement")

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
    print("7: List paintings by artist")
    print("8: List paintings by movement")

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
