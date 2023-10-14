# lib/cli.py

from termcolor import cprint

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
    list_paintings_by_movement,
    list_paintings_by_medium,
    display_artist_movement,
    list_artists_in_same_movement,
    list_artist_mediums
)

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
        choice = input("> ")
        if choice == "0":
            m = "artists"
        elif choice == "1":
            list_paintings_by_artist(artist)
        elif choice == "2":
            display_artist_movement(artist)
        elif choice == "3":
            list_artists_in_same_movement(artist)
        elif choice == "4":
            list_artist_mediums(artist)
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
            list_paintings_by_medium()
        elif choice == "8":
            painting = find_painting_by_id("return")
            if painting:
                explore_painting(painting) 
            else:
                cprint("Painting not found", "red")     
        else:
            print("Invalid choice")

def explore_painting(name):
    m = "explore painting"
    while m == "explore painting":
        painting_options_menu(name)
        choice = input("> ")
        if choice == "0":
            m = "paintings"
        elif choice == "1":
            pass
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
            find_movement_by_name()
        elif choice == "3":
            find_movement_by_id()
        elif choice == "4":
            create_movement()
        elif choice == "5":
            update_movement()
        elif choice == "6":
            delete_movement()
        elif choice == "7":
            movement = find_movement_by_name("return")
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
        choice = input("> ")
        if choice == "0":
            m = "movements"
        elif choice == "1":
            list_artists_by_movement(movement)
        elif choice == "2":
            list_paintings_by_movement(movement)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
