# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.painting import Painting

from helpers.helpers import (
    choose_medium, 
    divider
)

def list_paintings():
    divider()
    paintings = sorted(Painting.get_all(), key=lambda x: x.name)
    for painting in paintings:
        cprint(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")
    divider()

def choose_painting():
    id = input("Enter the painting's ID: ")
    paintings = sorted(Painting.get_all(), key=lambda x: x.name)
    try:
        return paintings[int(id) - 1]
    except:
        return None

# def find_painting_by_name():
#     name = input("Enter the painting's name: ")
#     paintings = Painting.find_by_name(name)
#     if paintings:
#         for painting in paintings:
#             cprint(painting, "green")
#     else:
#         cprint(f'Painting {name} not found', "red")

# def find_painting_by_id():
#     id_ = input("Enter the painting's id: ")
#     painting = Painting.find_by_id(id_)
#     return painting

def create_painting():
    name = input("Enter the painting's name: ")
    year = input("Enter the painting's year: ")
    print("Choose the painting's medium: ")
    medium = choose_medium()
    artist_id = input("Enter the painting's artist_id: ")
    try:
        painting = Painting.create(name, year, medium, artist_id)
        cprint(f'Creation successful: {painting}', "green")
    except Exception as exc:
        cprint(f"Error creating painting: {exc}", "red")

def update_painting(painting):
    try:
        name = input("Enter the painting's new name: ")
        painting.name = name
        year = input("Enter the painting's new year: ")
        painting.year = year
        print("Choose the painting's new medium: ")
        medium = choose_medium()
        painting.medium = medium
        artist_id = input("Enter the painting's new artist_id: ")
        painting.artist_id = artist_id

        painting.update()
        cprint(f"Update successful: {painting}", "green")
    except Exception as exc:
        cprint(f"Error updating painting: {exc}", "red")

def delete_painting(painting):
    confirmation_text = colored(
        "Are you sure you want to proceed? Y/N: ", 
        "yellow", 
        attrs=["bold"]
    )
    confirmation = input(confirmation_text)
    if confirmation == "y" or confirmation == "Y":
        painting.delete()
        cprint(f'{painting.name} deleted', "green")
        return "deleted"
    else:
        cprint("Deletion aborted", "green")
        return "aborted"

# def display_artist(painting):
#     artist = Artist.find_by_id(painting.artist_id)
#     cprint(artist, "green")

# def list_paintings_by_same_artist(painting):
#     artist = Artist.find_by_id(painting.artist_id)
#     paintings = [p for p in Painting.get_all() if p.artist_id == painting.artist_id]
#     other_paintings = [p for p in paintings if p.id != painting.id]
#     if other_paintings:
#         for painting in other_paintings:
#             cprint(painting, "green")
#     else:
#         cprint(f"No other paintings by {artist.name} found", "green")

def list_paintings_by_medium():
    print("Choose a medium: ")
    medium = choose_medium()
    if medium in Painting.mediums:
        paintings = [painting for painting in Painting.get_all() if painting.medium == medium]
        if paintings:
            for painting in paintings:
                cprint(painting, "green")
        else:
            cprint(f"No {medium} paintings found", "green")
    else:
        cprint("Invalid choice", "red")

# def list_paintings_by_year():
#     paintings = sorted(Painting.get_all(), key=lambda x: x.year)
#     for painting in paintings:
#         cprint(painting, "green")