# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.movement import Movement
from models.painting import Painting

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        cprint(artist, "green")

def find_artist_by_name():
    name = input("Enter the artist's name: ")
    artists = Artist.find_by_name(name)
    if artists:
        for artist in artists:
            cprint(artist, "green")
    else:
        cprint(f'Artist {name} not found', "red")

def find_artist_by_id(result="print"):
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if result == "print":
        cprint(artist, "green") if artist else cprint(f'Artist {id_} not found', "red")
    elif result == "return":
        return artist

def create_artist():
    name = input("Enter the artist's name: ")
    movement_id = input("Enter the artist's movement_id: ")
    try:
        artist = Artist.create(name, movement_id)
        cprint(f'Creation successful: {artist}', "green")
    except Exception as exc:
        cprint(f"Error creating artist: {exc}", "red")

def update_artist():
    id_ = input("Enter the artist's id: ")
    if artist := Artist.find_by_id(id_):
        try:
            name = input("Enter the artist's new name: ")
            artist.name = name
            movement_id = input("Enter the artist's new movement_id: ")
            artist.movement_id = movement_id

            artist.update()
            cprint(f"Update successful: {artist}", "green")
        except Exception as exc:
            cprint(f"Error updating artist: {exc}", "red")
    else:
        cprint(f'Artist {id_} not found', "red")

def delete_artist():
    id_ = input("Enter the artist's id: ")
    if artist := Artist.find_by_id(id_):
        confirmation_text = colored(
            "Deleting an artist will delete all associated paintings. Are you sure you want to proceed? Y/N: ", 
            "yellow", 
            attrs=["bold"]
        )
        confirmation = input(confirmation_text)
        if confirmation == "y" or confirmation == "Y":
            paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
            for painting in paintings:
                painting_id = painting.id
                painting.delete()
                cprint(f'Painting {painting_id} deleted', "green")
            artist.delete()
            cprint(f'Artist {id_} deleted', "green")
        else:
            cprint('Deletion aborted', "green")
    else:
        cprint(f'Artist {id_} not found', "red")

def list_paintings_by_artist(artist):
    paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
    if paintings:
        for painting in paintings:
            cprint(painting, "green")
    else:
        cprint(f'No paintings found by {artist.name}', "red")

def display_artist_movement(artist):
    movement = Movement.find_by_id(artist.movement_id)
    cprint(movement, "green")

def list_artists_in_same_movement(artist):
    movement = Movement.find_by_id(artist.movement_id)
    artists = [a for a in Artist.get_all() if a.movement_id == movement.id]
    other_artists = [a for a in artists if a.id != artist.id]
    if other_artists:
        for artist in other_artists:
            cprint(artist, "green")
    else:
        cprint(f'No other {movement.name} artists found', "red")

def list_artist_mediums(artist):
    mediums = [painting.medium for painting in Painting.get_all() if painting.artist_id == artist.id]
    cprint(", ".join(set(mediums)), "green")