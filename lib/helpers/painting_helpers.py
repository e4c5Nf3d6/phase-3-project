# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.painting import Painting

from helpers.general_helpers import spacer, error
from helpers.artist_helpers import choose_artist

def choose_medium(prompt="Choose a medium: "):
    for medium in Painting.mediums:
        print(f"{Painting.mediums.index(medium) + 1}. {medium}")
    spacer()
    choice = input(prompt)
    try:
        if int(choice) <= 0:
            raise ValueError
        medium = Painting.mediums[int(choice) - 1]
        return medium
    except:
        error()

def list_paintings():
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    if paintings:
        for painting in paintings:
            cprint(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")
    else:
        cprint("No paintings found", "red")

def choose_painting():
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    if paintings:
        for painting in paintings:
            print(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}")
        spacer()
        id = input("Choose a painting: ")
        try:
            if int(id) <= 0:
                raise ValueError
            return paintings[int(id) - 1]
        except:
            error()
    else:
        cprint("No paintings found", "red")

def create_painting(artist_id=None):
    name = input("Enter the painting's name: ")
    year = input("Enter the painting's year: ")
    spacer()
    medium = choose_medium("Choose the painting's medium: ")

    if not medium:
        return None
    
    if not artist_id:
        try:
            artist_id = choose_artist("Choose the painting's artist: ").id
        except:
            return None
        
    spacer()
    try:
        painting = Painting.create(name, year, medium, artist_id)
        cprint(f'{painting.name} successfully created', "green")
        return painting
    except Exception as exc:
        cprint(f"Error creating painting: {exc}", "red")

def update_painting(painting):
    original_name = painting.name
    original_year = painting.year
    original_medium = painting.medium
    try:
        name = input("Enter the painting's new name: ")
        year = input("Enter the painting's new year: ")
        spacer()
        medium = choose_medium("Choose the painting's new medium: ")

        if not medium:
            return None
        
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
        painting.name = original_name
        painting.year = original_year
        painting.medium = original_medium
        spacer()
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
