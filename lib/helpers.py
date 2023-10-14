# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.movement import Movement
from models.painting import Painting

def exit_program():
    print("Goodbye!")
    exit()

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        cprint(artist, "green")

def find_artist_by_name():
    name = input("Enter the artist's name: ")
    artist = Artist.find_by_name(name)
    cprint(artist, "green") if artist else cprint(f'Artist {name} not found', "red")

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

def list_paintings():
    paintings = Painting.get_all()
    for painting in paintings:
        cprint(painting, "green")

def find_painting_by_name():
    name = input("Enter the painting's name: ")
    painting = Painting.find_by_name(name)
    cprint(painting, "green") if painting else cprint(f'Painting {name} not found', "red")

def find_painting_by_id(result="print"):
    id_ = input("Enter the painting's id: ")
    painting = Painting.find_by_id(id_)
    if result == "print":
        cprint(painting, "green") if painting else cprint(f'Painting {id_} not found', "red")
    elif result == "return":
        return painting

def create_painting():
    name = input("Enter the painting's name: ")
    year = input("Enter the painting's year: ")
    medium = input("Enter the painting's medium: ")
    artist_id = input("Enter the painting's artist_id: ")
    try:
        painting = Painting.create(name, year, medium, artist_id)
        cprint(f'Creation successful: {painting}', "green")
    except Exception as exc:
        cprint(f"Error creating painting: {exc}", "red")

def update_painting():
    id_ = input("Enter the painting's id: ")
    if painting := Painting.find_by_id(id_):
        try:
            name = input("Enter the painting's new name: ")
            painting.name = name
            year = input("Enter the painting's new year: ")
            painting.year = year
            medium = input("Enter the painting's new medium: ")
            painting.medium = medium
            artist_id = input("Enter the painting's new artist_id: ")
            painting.artist_id = artist_id

            painting.update()
            cprint(f"Update successful: {painting}", "green")
        except Exception as exc:
            cprint(f"Error updating painting: {exc}", "red")
    else:
        cprint(f'Painting {id_} not found', "red")

def delete_painting():
    id_ = input("Enter the painting's id: ")
    if painting := Painting.find_by_id(id_):
        confirmation_text = colored(
            "Are you sure you want to proceed? Y/N: ", 
            "yellow", 
            attrs=["bold"]
        )
        confirmation = input(confirmation_text)
        if confirmation == "y" or confirmation == "Y":
            painting.delete()
            cprint(f'Painting {id_} deleted', "green")
        else:
            cprint("Deletion aborted", "green")
    else:
        cprint(f'Painting {id_} not found', "red")

def list_movements():
    movements = Movement.get_all()
    for movement in movements:
        cprint(movement, "green")

def find_movement_by_name(result="print"):
    name = input("Enter the movement's name: ")
    movement = Movement.find_by_name(name)
    if result == "print":
        cprint(movement, "green") if movement else cprint(f'Movement {name} not found', "red")
    elif result == "return":
        return movement

def find_movement_by_id():
    id_ = input("Enter the movement's id: ")
    movement = Movement.find_by_id(id_)
    cprint(movement, "green") if movement else cprint(f'Movement {id_} not found', "red")

def create_movement():
    name = input("Enter the movement's name: ")
    try:
        movement = Movement.create(name)
        cprint(f'Creation successful: {movement}', "green")
    except Exception as exc:
        cprint(f"Error creating movement: {exc}", "red")

def update_movement():
    id_ = input("Enter the movement's id: ")
    if movement := Movement.find_by_id(id_):
        try:
            name = input("Enter the movement's new name: ")
            movement.name = name

            movement.update()
            cprint(f"Update successful: {movement}", "green")
        except Exception as exc:
            cprint(f"Error updating movement: {exc}", "red")
    else:
        cprint(f'Movement {id_} not found', "red")

def delete_movement():
    id_ = input("Enter the movement's id: ")
    if movement := Movement.find_by_id(id_):
        confirmation_text = colored(
            "Deleting a movement will delete all associated artists and paintings. Are you sure you want to proceed? Y/N: ", 
            "red", 
            attrs=["bold"]
        )
        confirmation = input(confirmation_text)
        if confirmation == "y" or confirmation == "Y":
            artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
            for artist in artists:
                artist_id = artist.id
                paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
                for painting in paintings:
                    painting_id = painting.id
                    painting.delete()
                    cprint(f'Painting {painting_id} deleted', "green")
                artist.delete()
                cprint(f'Artist {artist_id} deleted', "green")
            movement.delete()
            cprint(f'Movement {id_} deleted', "green")
        else:
            cprint("Deletion aborted", "green")
    else:
        cprint(f'Movement {id_} not found', "red")

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

def list_artists_by_movement(movement):
    artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
    if artists:
        for artist in artists:
            cprint(artist, "green")
    else:
        cprint(f'No {movement.name} artists found', "red")

def display_artist(painting):
    artist = Artist.find_by_id(painting.artist_id)
    cprint(artist, "green")

def list_paintings_by_same_artist(painting):
    artist = Artist.find_by_id(painting.artist_id)
    paintings = [p for p in Painting.get_all() if p.artist_id == painting.artist_id]
    other_paintings = [p for p in paintings if p.id != painting.id]
    if other_paintings:
        for painting in other_paintings:
            cprint(painting, "green")
    else:
        cprint(f"No other paintings by {artist.name} found", "red")

def list_paintings_by_movement(movement):
    artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
    if artists:
        for artist in artists:
            paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
            if paintings:
                for painting in paintings:
                    cprint(painting, "green")
            else:
                cprint(f"No {movement.name} paintings found", "red")
    else:
        cprint(f"No {movement.name} paintings found", "red")

def list_paintings_by_medium():
    medium = input("Enter medium: ")
    if medium in Painting.mediums:
        paintings = [painting for painting in Painting.get_all() if painting.medium == medium]
        if paintings:
            for painting in paintings:
                cprint(painting, "green")
        else:
            cprint(f"No {medium} paintings found", "green")
    else:
        cprint(f"{medium} is not a valid medium. Valid mediums: acrylic, encaustic, fresco, oil, tempera, watercolor", "red")