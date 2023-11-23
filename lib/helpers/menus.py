from termcolor import cprint

from models.movement import Movement
from models.artist import Artist

from helpers.general_helpers import (
    divider,
    spacer
)

def main_menu():
    divider()
    cprint("Main Menu", "cyan")
    spacer()
    print("0. Exit the program")
    print("1. Movements")
    print("2. Artists")
    print("3. Paintings")
    divider()


def artists_menu():
    divider()
    cprint("Artists Menu", "cyan")
    spacer()
    print("0. Return to main menu")
    print("1. List all artists")
    print("2. Add a new artist")
    print("3. Explore an artist")
    divider()

def artist_options_menu(artist):
    divider()
    cprint(f"Exploring artist: {artist.name}", "cyan")
    print(f"   Movement: {Movement.find_by_id(artist.movement_id).name}")
    spacer()
    print("0. Go back to the previous menu")
    print(f"1. List paintings by {artist.name}")
    print(f"2. Explore a painting by {artist.name}")
    print(f"3. Add a new {artist.name} painting")
    print(f"4. Update {artist.name}")
    print(f"5. Delete {artist.name}")
    divider()

def paintings_menu():
    divider()
    cprint("Paintings Menu", "cyan")
    spacer()
    print("0. Go back to main menu")
    print("1. List all paintings")
    print("2. List paintings by medium")
    print("3. Create painting")
    print("4. Explore a painting")
    divider()

def painting_options_menu(painting):
    divider()
    cprint(f"Exploring painting: {painting.name}", "cyan")
    print(f"  Artist: {Artist.find_by_id(painting.artist_id).name}")
    print(f"  Year: {painting.year}")
    print(f"  Medium: {painting.medium}")
    spacer()
    print("0. Go back to the previous menu")
    print(f"1. Update {painting.name}")
    print(f"2. Delete {painting.name}")
    divider()

def movements_menu():
    divider()
    cprint("Movements Menu", "cyan")
    spacer()
    print("0. Go back to main menu")
    print("1. List all movements")
    print("2. Create movement")
    print("3. Explore a movement")
    divider()

def movement_options_menu(movement):
    divider()
    cprint(f"Exploring movement: {movement.name}", "cyan")
    print(f"  Year founded: {movement.year_founded}")
    spacer()
    print("0. Go back to the previous menu")
    print(f"1. List artists in the {movement.name} movement")
    print(f"2. Explore an artist in the {movement.name} movement")
    print(f"3. Add a new {movement.name} artist")
    print("4. Update movement")
    print("5. Delete movement")
    divider()