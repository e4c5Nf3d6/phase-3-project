# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.painting import Painting

from helpers.general_helpers import spacer, error
from helpers.movement_helpers import choose_movement

def list_artists():
    if Artist.get_all():
        artists = sorted(Artist.get_all(), key=lambda x: x.name.lower())
        for artist in artists:
            cprint(f"{artists.index(artist) + 1}. {artist.name}", "green")
    else:
        cprint("No artists found", "red")

def choose_artist(prompt="Choose an artist: "):
    if Artist.get_all():
        artists = sorted(Artist.get_all(), key=lambda x: x.name.lower())
        for artist in artists:
            print(f"{artists.index(artist) + 1}. {artist.name}")
        spacer()
        id = input(prompt)
        try:
            if int(id) <= 0:
                raise ValueError
            return artists[int(id) - 1]
        except:
            error()  
    else:
        cprint("No artists found", "red")

def create_artist(movement_id=None):
    name = input("Enter the artist's name: ")
    spacer()
    if not movement_id:
        try:
            movement_id = choose_movement("Choose the artist's movement: ").id
            spacer()
        except:
            return None
    try:
        artist = Artist.create(name, movement_id)
        cprint(f'{artist.name} created successfully', "green")
        return artist
    except Exception as exc:
        cprint(f"Error creating artist: {exc}", "red")

def update_artist(artist):
    try:
        name = input("Enter the artist's new name: ")
        movement = choose_movement("Choose the artist's new movement: ")

        if movement:
            artist.name = name
            artist.movement_id = movement.id

            artist.update()
            spacer()
            cprint(f"{artist.name} updated successfully", "green")
    except Exception as exc:
        spacer()
        cprint(f"Error updating artist: {exc}", "red")

def delete_artist(artist):
    confirmation_text = colored(
        "Deleting an artist will delete all associated paintings. Are you sure you want to proceed? Y/N: ", 
        "yellow", 
        attrs=["bold"]
    )
    spacer()
    confirmation = input(confirmation_text)
    spacer()
    if confirmation == "y" or confirmation == "Y":
        paintings = Painting.find_by_artist(artist.id)
        if paintings:
            for painting in paintings:
                painting.delete()
        artist.delete()
        cprint(f'{artist.name} deleted', "green")
        return "deleted"
    else:
        cprint('Deletion aborted', "green")

def list_paintings_by_artist(artist):
    if Painting.find_by_artist(artist.id):
        paintings = sorted(Painting.find_by_artist(artist.id), key=lambda x: x.name.lower())
        for painting in paintings:
            cprint(f"{paintings.index(painting) + 1}. {painting.name}", "green")
    else:
        cprint(f'No paintings by {artist.name} found', "red")

def choose_painting_by_artist(artist):
    if Painting.find_by_artist(artist.id):
        paintings = sorted(Painting.find_by_artist(artist.id), key=lambda x: x.name.lower())
        for painting in paintings:
            print(f"{paintings.index(painting) + 1}. {painting.name}")
        spacer()
        id = input("Enter the painting's ID: ")
        try:
            if int(id) <= 0:
                raise ValueError
            return paintings[int(id) - 1]
        except:
            error()
    else:
        spacer()
        cprint(f"No paintings by {artist.name} found", "red")