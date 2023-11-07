# lib/cli.py

from termcolor import cprint

from helpers.artist_helpers import (
    list_artists,
    choose_artist,
    create_artist,
    update_artist,
    delete_artist,
    list_paintings_by_artist,
)

from helpers.movement_helpers import (
    list_movements,
    choose_movement,
    create_movement,
    update_movement,
    delete_movement,
    list_artists_by_movement,
    list_paintings_by_movement,
)

from helpers.painting_helpers import (
    list_paintings,
    choose_painting,
    create_painting,
    update_painting,
    delete_painting,
    list_paintings_by_medium,
)

from helpers.general_helpers import (
    exit_program,
    spacer
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
            spacer()
            cprint("Invalid choice", "red")

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
            artist = choose_artist()
            if artist:
                explore_artist(artist) 
            else:
                spacer()
                cprint("Invalid choice", "red")   
        else:
            spacer()
            cprint("Invalid choice", "red")

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
            create_painting(artist.id)
        elif choice == "3":
            update_artist(artist)
        elif choice == "4":
            result = delete_artist(artist)
            if result == "deleted":
                m = "artists"
        else:
            spacer()
            cprint("Invalid choice", "red")

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
            list_paintings_by_medium()        
        elif choice == "3":
            create_painting()
        elif choice == "4":
            painting = choose_painting()
            if painting:
                explore_painting(painting) 
            else:
                spacer()
                cprint("Invalid Choice", "red")     
        else:
            spacer()
            cprint("Invalid choice", "red")

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
            spacer()
            cprint("Invalid choice", "red")

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
            movement = choose_movement()
            if movement:
                explore_movement(movement) 
            else:
                spacer()
                cprint("Invalid choice", "red")           
        else:
            spacer()
            cprint("Invalid choice", "red")

def explore_movement(movement):
    m = "explore movement"
    while m == "explore movement":
        movement_options_menu(movement)
        choice = input("Enter your choice: ")
        if choice == "0":
            m = "movements"
        elif choice == "1":
            list_artists_by_movement(movement)
        elif choice == "2":
            create_artist(movement.id)
        elif choice == "3":
            update_movement(movement)
        elif choice == "4":
            result = delete_movement(movement)
            if result == "deleted":
                m = "movements"
        else:
            spacer()
            cprint("Invalid choice", "red")

if __name__ == "__main__":
    main()
