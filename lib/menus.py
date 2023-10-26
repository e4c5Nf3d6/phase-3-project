from termcolor import cprint

def main_menu():
    cprint("Main Menu", "cyan")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Artists")
    print("2. Paintings")
    print("3. Movements")

def artists_menu():
    cprint("Artist Menu", "cyan")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. List all artists")
    print("2. Find artist by name")
    print("3. Find artist by id")
    print("4. Create artist")
    print("5. Update artist")
    print("6. Delete artist")
    print("7. Explore an artist")

def artist_options_menu(artist):
    cprint(f"Exploring: {artist}", "cyan")
    print("Please select an option:")
    print("0. Go back to artist menu")
    print("1. List paintings by this artist")
    print("2. Display artist's movement")
    print("3. List other artists in the same movement")
    print("4. List mediums used by this artist")

def paintings_menu():
    cprint("Paintings Menu", "cyan")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. List all paintings")
    print("2. Find painting by name")
    print("3. Find painting by id")
    print("4. Create painting")
    print("5. Update painting")
    print("6. Delete painting")
    print("7. List paintings by medium")
    print("8. List paintings chronologically")
    print("9. Explore a painting")

def painting_options_menu(painting):
    cprint(f"Exploring: {painting}", "cyan")
    print("Please select an option:")
    print("0. Go back to paintings menu")
    print("1. Display this painting's artist")
    print("2. Display other paintings by this artist")

def movements_menu():
    cprint("Movements Menu", "cyan")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. List all movements")
    print("2. Find movement by name")
    print("3. Find movement by id")
    print("4. Create movement")
    print("5. Update movement")
    print("6. Delete movement")
    print("7. List movements chronologically")
    print("8. Explore a movement")

def movement_options_menu(movement):
    cprint(f"Exploring: {movement}", "cyan")
    print("Please select an option:")
    print("0. Go back to movements menu")
    print("1. Display artists in this movement")
    print("2. Display paintings in this movement")