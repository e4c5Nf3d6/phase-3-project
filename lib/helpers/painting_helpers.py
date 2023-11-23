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
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    for painting in paintings:
        cprint(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")

def choose_painting():
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    if paintings:
        for painting in paintings:
            print(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}")
        spacer()
        id = input("Choose a painting: ")
        try:
            if int(id) == 0:
                raise ValueError
            return paintings[int(id) - 1]
        except:
            spacer()
            cprint("Invalid choice", "red")
    else:
        cprint("No paintings found", "red")

def create_painting(artist_id=None):
    name = input("Enter the painting's name: ")
    year = input("Enter the painting's year: ")
    spacer()
    medium = choose_medium("Choose the painting's medium: ")
    if not artist_id:
        try:
            artist_id = choose_artist("Choose the painting's artist: ").id
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
    try:
        name = input("Enter the painting's new name: ")
        year = input("Enter the painting's new year: ")
        spacer()
        medium = choose_medium("Choose the painting's new medium: ")
        artist = choose_artist("Choose the painting's new artist: ")

        if artist:
            painting.name = name
            painting.year = year       
            painting.medium = medium
            painting.artist_id = artist.id

            painting.update()
            spacer()
            cprint(f"{painting.name} successfully updated", "green")
    
    except Exception as exc:
        cprint(f"Error updating painting: {exc}", "red")

def delete_painting(painting):
    confirmation_text = colored(
        "Are you sure you want to proceed? Y/N: ", 
        "yellow", 
        attrs=["bold"]
    )
    confirmation = input(confirmation_text)
    spacer()
    if confirmation == "y" or confirmation == "Y":
        painting.delete()
        cprint(f'{painting.name} successfully deleted', "green")
        return "deleted"
    else:
        cprint("Deletion aborted", "green")

def list_paintings_by_medium():
    medium = choose_medium()
    spacer()
    if medium in Painting.mediums:
        paintings = [painting for painting in Painting.get_all() if painting.medium == medium]
        if paintings:
            for painting in paintings:
                cprint(f"{painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")
        else:
            cprint(f"No {medium} paintings found", "red")
    else:
        cprint("Invalid choice", "red")