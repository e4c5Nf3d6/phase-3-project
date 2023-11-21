# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.painting import Painting

from helpers.general_helpers import (
    choose_medium, 
    spacer
)

from helpers.artist_helpers import choose_artist

def list_paintings():
    spacer()
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    for painting in paintings:
        cprint(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")
    spacer()

def choose_painting():
    spacer()
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    for painting in paintings:
        print(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}")
    spacer()
    id = input("Enter the painting's ID: ")
    try:
        if int(id) == 0:
            raise ValueError
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

def create_painting(artist_id=None):
    name = input("Enter the painting's name: ")
    year = input("Enter the painting's year: ")
    print("Choose the painting's medium: ")
    medium = choose_medium()
    if not artist_id:
        try:
            artist_id = choose_artist().id
        except:
            cprint("Invalid choice", "red")
            return None
    spacer()
    try:
        painting = Painting.create(name, year, medium, artist_id)
        cprint(f'{painting.name} successfully created', "green")
        return painting
    except Exception as exc:
        cprint(f"Error creating painting: {exc}", "red")
        return None

def update_painting(painting):
    spacer()
    try:
        name = input("Enter the painting's new name: ")
        year = input("Enter the painting's new year: ")
        print("Choose the painting's new medium: ")
        medium = choose_medium()
        artist = choose_artist()

        if artist:
            painting.name = name
            painting.year = year       
            painting.medium = medium
            painting.artist_id = artist.id

            painting.update()
            cprint(f"{painting.name} successfully updated", "green")
        else:
            raise Exception("Invalid artist choice")
    except Exception as exc:
        cprint(f"Error updating painting: {exc}", "red")

def delete_painting(painting):
    confirmation_text = colored(
        "Are you sure you want to proceed? Y/N: ", 
        "yellow", 
        attrs=["bold"]
    )
    spacer()
    confirmation = input(confirmation_text)
    spacer()
    if confirmation == "y" or confirmation == "Y":
        painting.delete()
        cprint(f'{painting.name} successfully deleted', "green")
        return "deleted"
    else:
        cprint("Deletion aborted", "green")

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
    spacer()
    if medium in Painting.mediums:
        paintings = [painting for painting in Painting.get_all() if painting.medium == medium]
        if paintings:
            for painting in paintings:
                cprint(f"{painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")
        else:
            cprint(f"No {medium} paintings found", "green")
    else:
        cprint("Invalid choice", "red")

# def list_paintings_by_year():
#     paintings = sorted(Painting.get_all(), key=lambda x: x.year)
#     for painting in paintings:
#         cprint(painting, "green")