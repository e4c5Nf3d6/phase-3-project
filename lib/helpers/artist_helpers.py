# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.painting import Painting

from helpers.general_helpers import spacer

from helpers.movement_helpers import choose_movement

def list_artists():
    spacer()
    artists = sorted(Artist.get_all(), key=lambda x: x.name.lower())
    for artist in artists:
        cprint(f"{artists.index(artist) + 1}. {artist.name}", "green")
    spacer()

def choose_artist():
    spacer()
    artists = sorted(Artist.get_all(), key=lambda x: x.name.lower())
    for artist in artists:
        print(f"{artists.index(artist) + 1}. {artist.name}")
    spacer()
    id = input("Enter the artist's ID: ")
    artists = sorted(Artist.get_all(), key=lambda x: x.name.lower())
    try:
        if int(id) == 0:
            raise ValueError
        return artists[int(id) - 1]
    except:
        return None
    
# def find_artist_by_name():
#     name = input("Enter the artist's name: ")
#     artists = Artist.find_by_name(name)
#     if artists:
#         for artist in artists:
#             cprint(artist, "green")
#     else:
#         cprint(f'Artist {name} not found', "red")

def create_artist(movement_id=None):
    name = input("Enter the artist's name: ")
    spacer()
    if not movement_id:
        try:
            movement_id = choose_movement().id
        except:
            cprint("Invalid choice", "red")
            return None
    try:
        artist = Artist.create(name, movement_id)
        cprint(f'{artist.name} created successfully', "green")
        return artist
    except Exception as exc:
        cprint(f"Error creating artist: {exc}", "red")
        return None

def update_artist(artist):
    spacer()
    try:
        name = input("Enter the artist's new name: ")
        artist.name = name
        movement_id = choose_movement().id
        artist.movement_id = movement_id

        artist.update()
        cprint(f"{artist.name} updated successfully", "green")
    except Exception as exc:
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
        paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
        for painting in paintings:
            painting.delete()
        artist.delete()
        cprint(f'{artist.name} deleted', "green")
        return "deleted"
    else:
        cprint('Deletion aborted', "green")

def list_paintings_by_artist(artist):
    paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
    if paintings:
        spacer()
        for painting in paintings:
            cprint(f"{painting.name}, {painting.year}", "green")
        spacer()
    else:
        spacer()
        cprint(f'No paintings found by {artist.name}', "green")

# def display_artist_movement(artist):
#     movement = Movement.find_by_id(artist.movement_id)
#     cprint(movement, "green")

# def list_artists_in_same_movement(artist):
#     movement = Movement.find_by_id(artist.movement_id)
#     artists = [a for a in Artist.get_all() if a.movement_id == movement.id]
#     other_artists = [a for a in artists if a.id != artist.id]
#     if other_artists:
#         for artist in other_artists:
#             cprint(artist, "green")
#     else:
#         cprint(f'No other {movement.name} artists found', "green")

# def list_artist_mediums(artist):
#     mediums = [painting.medium for painting in Painting.get_all() if painting.artist_id == artist.id]
#     if mediums:
#         cprint(", ".join(set(mediums)), "green")
#     else:
#         cprint(f"No mediums recorded for {artist.name}", "green")