from termcolor import cprint

from helpers.helpers import spacer

def main_menu():
    spacer()
    cprint("Main Menu", "cyan")
    print("0. Exit the program")
    print("1. Artists")
    print("2. Paintings")
    print("3. Movements")
    spacer()


def artists_menu():
    spacer()
    cprint("Artist Menu", "cyan")
    print("0. Return to main menu")
    print("1. List all artists")
    print("2. Add a new artist")
    print("3. Explore an artist")
    spacer()

def artist_options_menu(artist):
    spacer()
    cprint(f"Exploring {artist.name}", "cyan")
    print("0. Go back to the artists menu")
    print(f"1. List paintings by {artist.name}")
    print(f"2. Update {artist.name}")
    print(f"3. Delete {artist.name}")
    spacer()

def paintings_menu():
    spacer()
    cprint("Paintings Menu", "cyan")
    print("0. Go back to main menu")
    print("1. List all paintings")
    print("2. Create painting")
    print("3. List paintings by medium")
    print("4. Explore a painting")
    spacer()

def painting_options_menu(painting):
    spacer()
    cprint(f"Exploring {painting}", "cyan")
    print("0. Go back to paintings menu")
    print(f"1. Update {painting.name}")
    print(f"2. Delete {painting.name}")
    spacer()

def movements_menu():
    spacer()
    cprint("Movements Menu", "cyan")
    print("0. Go back to main menu")
    print("1. List all movements")
    print("4. Create movement")
    print("8. Explore a movement")
    spacer()

def movement_options_menu(movement):
    spacer()
    cprint(f"Exploring {movement}", "cyan")
    print("0. Go back to movements menu")
    print("1. Update Movement")
    print("1. Delete movement")
    print("1. List artists in this movement")
    print("2. List paintings in this movement")
    spacer()