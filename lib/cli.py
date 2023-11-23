# lib/cli.py

from termcolor import cprint

from helpers.menus import (
    main_menu,
    artists_menu,
    paintings_menu,
    movements_menu,
    artist_options_menu,
    painting_options_menu,
    movement_options_menu
)

from helpers.general_helpers import (
    exit_program,
    spacer
)

from helpers.movement_helpers import (
    list_movements,
    choose_movement,
    create_movement,
    update_movement,
    delete_movement,
    list_artists_by_movement
)

from helpers.artist_helpers import (
    list_artists,
    choose_artist,
    create_artist,
    update_artist,
    delete_artist,
    list_paintings_by_artist,
    choose_artist_by_movement
)

from helpers.painting_helpers import (
    list_paintings,
    choose_painting,
    create_painting,
    update_painting,
    delete_painting,
    list_paintings_by_medium,
    choose_painting_by_artist
)

def main():
    m = "main"
    while m == "main":
        main_menu()
        choice = input("Enter your choice: ")
        spacer()
        if choice == "0":
            exit_program()
        elif choice == "1":
            movements()
        elif choice == "2":
            artists()
        elif choice == "3":
            paintings()
        else:
            cprint("Invalid choice", "red")

def movements():
    m = "movements"
    while m == "movements":
        movements_menu()
        choice = input("Enter your choice: ")
        spacer()
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_movements()
        elif choice == "2":
            movement = create_movement()
            if movement:
                explore_movement(movement)
        elif choice == "3":
            movement = choose_movement()
            if movement:
                explore_movement(movement)     
        else:
            cprint("Invalid choice", "red")

def explore_movement(movement):
    m = "explore movement"
    while m == "explore movement":
        movement_options_menu(movement)
        choice = input("Enter your choice: ")
        spacer()
        if choice == "0":
            m = ""
        elif choice == "1":
            list_artists_by_movement(movement)
        elif choice == "2":
            artist = choose_artist_by_movement(movement)
            if artist:
                explore_artist(artist)            
        elif choice == "3":
            artist = create_artist(movement.id)
            if artist:
                explore_artist(artist)
        elif choice == "4":
            update_movement(movement)
        elif choice == "5":
            result = delete_movement(movement)
            if result == "deleted":
                m = "movements"
        else:
            cprint("Invalid choice", "red")

def artists():
    m = "artists"
    while m == "artists":
        artists_menu()
        choice = input("Enter your choice: ")
        spacer()
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_artists()
        elif choice == "2":
            artist = create_artist()
            if artist:
                explore_artist(artist)
        elif choice == "3":
            artist = choose_artist()
            if artist:
                explore_artist(artist)
        else:
            cprint("Invalid choice", "red")

def explore_artist(artist):
    m = "explore artist"
    while m == "explore artist":
        artist_options_menu(artist)
        choice = input("Enter your choice: ")
        spacer()
        if choice == "0":
            m = ""
        elif choice == "1":
            list_paintings_by_artist(artist)
        elif choice == "2":
            painting = choose_painting_by_artist(artist)
            if painting:
                explore_painting(painting) 
        elif choice == "3":
            painting = create_painting(artist.id)
            if painting:
                explore_painting(painting)
        elif choice == "4":
            update_artist(artist)
        elif choice == "5":
            result = delete_artist(artist)
            if result == "deleted":
                m = "artists"
        else:
            cprint("Invalid choice", "red")

def paintings():
    m = "paintings"
    while m == "paintings":
        paintings_menu()
        choice = input("Enter your choice: ")
        spacer()
        if choice == "0":
            m = "main"
        elif choice == "1":
            list_paintings()
        elif choice == "2":
            list_paintings_by_medium()        
        elif choice == "3":
            painting = create_painting()
            if painting:
                explore_painting(painting)
        elif choice == "4":
            painting = choose_painting()
            if painting:
                explore_painting(painting)     
        else:
            cprint("Invalid choice", "red")

def explore_painting(painting):
    m = "explore painting"
    while m == "explore painting":
        painting_options_menu(painting)
        choice = input("Enter your choice: ")
        spacer()
        if choice == "0":
            m = ""
        elif choice == "1":
            update_painting(painting)
        elif choice == "2":
            result = delete_painting(painting)
            if result == "deleted":
                m = "paintings"
        else:
            cprint("Invalid choice", "red")

if __name__ == "__main__":
    main()
