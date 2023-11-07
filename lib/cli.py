# lib/cli.py

from termcolor import cprint

from helpers.artist_helpers import (
    list_artists,
    find_artist_by_name,
    find_artist_by_id,
    create_artist,
    update_artist,
    delete_artist,
    list_paintings_by_artist,
    display_artist_movement,
    list_artists_in_same_movement,
    list_artist_mediums
)

from helpers.movement_helpers import (
    list_movements,
    find_movement_by_name,
    find_movement_by_id,
    create_movement,
    update_movement,
    delete_movement,
    list_artists_by_movement,
    list_paintings_by_movement,
    list_movements_by_year
)

from helpers.painting_helpers import (
    list_paintings,
    find_painting_by_id,
    find_painting_by_name,
    create_painting,
    update_painting,
    delete_painting,
    display_artist,
    list_paintings_by_same_artist,
    list_paintings_by_medium,
    list_paintings_by_year
)

from helpers.helpers import exit_program

from menus import (
    main_menu,
    artists_menu,
    paintings_menu,
    movements_menu,
    artist_options_menu,
    painting_options_menu,
    movement_options_menu
)

def main():
    m = "main"
    while m == "main":
        main_menu()
        choice = input("Enter your choice: ")
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
        choice = input("Enter your choice: ")
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_artists()
        elif choice == "2":
            create_artist()
        elif choice == "3":
            artist = find_artist_by_id("return")
            if artist:
                explore_artist(artist) 
            else:
                cprint("Artist not found", "red")   
        else:
            print("Invalid choice")

def explore_artist(artist):
    m = "explore artist"
    while m == "explore artist":
        artist_options_menu(artist)
        choice = input("Enter your choice: ")
        if choice == "0":
            m = "artists"
        elif choice == "1":
            list_paintings_by_artist(artist)
        elif choice == "2":
            update_artist(artist)
        elif choice == "3":
            result = delete_artist(artist)
            if result == "deleted":
                m = "artists"
        else:
            print("Invalid choice")

def paintings():
    m = "paintings"
    while m == "paintings":
        paintings_menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_paintings()
        elif choice == "2":
            create_painting()
        elif choice == "3":
            list_paintings_by_medium()
        elif choice == "4":
            painting = find_painting_by_id("return")
            if painting:
                explore_painting(painting) 
            else:
                cprint("Painting not found", "red")     
        else:
            print("Invalid choice")

def explore_painting(painting):
    m = "explore painting"
    while m == "explore painting":
        painting_options_menu(painting)
        choice = input("Enter your choice: ")
        if choice == "0":
            m = "paintings"
        elif choice == "1":
            update_painting(painting)
        elif choice == "2":
            result = delete_painting(painting)
            if result == "deleted":
                m = "paintings"
        else:
            print("Invalid choice")

def movements():
    m = "movements"
    while m == "movements":
        movements_menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_movements()
        elif choice == "2":
            create_movement()
        elif choice == "3":
            movement = find_movement_by_id("return")
            if movement:
                explore_movement(movement) 
            else:
                cprint("Movement not found", "red")           
        else:
            print("Invalid choice")

def explore_movement(movement):
    m = "explore movement"
    while m == "explore movement":
        movement_options_menu(movement)
        choice = input("Enter your choice: ")
        if choice == "0":
            m = "movements"
        elif choice == "1":
            update_movement(movement)
        elif choice == "2":
            result = delete_movement(movement)
            if result == "deleted":
                m = "movements"
        elif choice == "3":
            list_artists_by_movement(movement)
        elif choice == "4":
            list_paintings_by_movement(movement)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
