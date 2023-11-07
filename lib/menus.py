from termcolor import cprint

def main_menu():
    cprint("Main Menu", "cyan")
    print("0. Exit the program")
    print("1. Artists")
    print("2. Paintings")
    print("3. Movements")

def artists_menu():
    cprint("Artist Menu", "cyan")
    print("0. Return to main menu")
    print("1. List all artists")
    print("2. Add a new artist")
    print("3. Explore an artist")

def artist_options_menu(artist):
    cprint(f"Exploring {artist.name}", "cyan")
    print("0. Go back to the artists menu")
    print(f"1. List paintings by {artist.name}")
    print(f"2. Update {artist.name}")
    print(f"3. Delete {artist.name}")

def paintings_menu():
    cprint("Paintings Menu", "cyan")
    print("0. Go back to main menu")
    print("1. List all paintings")
    print("2. Create painting")
    print("3. List paintings by medium")
    print("4. Explore a painting")

def painting_options_menu(painting):
    cprint(f"Exploring: {painting}", "cyan")
    print("0. Go back to paintings menu")
    print(f"1. Update {painting.name}")
    print(f"2. Delete {painting.name}")

def movements_menu():
    cprint("Movements Menu", "cyan")
    print("0. Go back to main menu")
    print("1. List all movements")
    print("4. Create movement")
    print("8. Explore a movement")

def movement_options_menu(movement):
    cprint(f"Exploring: {movement}", "cyan")
    print("0. Go back to movements menu")
    print("1. Update Movement")
    print("1. Delete movement")
    print("1. List artists in this movement")
    print("2. List paintings in this movement")