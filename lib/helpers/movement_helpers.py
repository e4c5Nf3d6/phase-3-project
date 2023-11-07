# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.movement import Movement
from models.painting import Painting

from helpers.helpers import divider

def list_movements():
    divider()
    movements = sorted(Movement.get_all(), key=lambda x: x.name)
    for movement in movements:
        cprint(f"{movements.index(movement) + 1}. {movement.name}", "green")
    divider()

def choose_movement():
    id = input("Enter the movement's ID: ")
    movements = sorted(Movement.get_all(), key=lambda x: x.name)
    try:
        return movements[int(id) - 1]
    except:
        return None

# def find_movement_by_name():
#     name = input("Enter the movement's name: ")
#     movement = Movement.find_by_name(name)
#     cprint(movement, "green") if movement else cprint(f'Movement {name} not found', "red")

# def find_movement_by_id():
#     id_ = input("Enter the movement's id: ")
#     movement = Movement.find_by_id(id_)
#     return movement

def create_movement():
    name = input("Enter the movement's name: ")
    year_founded = input("Enter the movement's founding year: ")
    try:
        movement = Movement.create(name, year_founded)
        cprint(f'Creation successful: {movement}', "green")
    except Exception as exc:
        cprint(f"Error creating movement: {exc}", "red")

def update_movement(movement):
    try:
        name = input("Enter the movement's new name: ")
        movement.name = name
        year_founded = input("Enter the movement's new founding year: ")
        movement.year_founded = year_founded

        movement.update()
        cprint(f"Update successful: {movement}", "green")
    except Exception as exc:
        cprint(f"Error updating movement: {exc}", "red")

def delete_movement(movement):
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
        cprint(f'{movement.name} deleted', "green")
    else:
        cprint("Deletion aborted", "green")

def list_artists_by_movement(movement):
    artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
    if artists:
        for artist in artists:
            cprint(artist, "green")
    else:
        cprint(f'No {movement.name} artists found', "red")

def list_paintings_by_movement(movement):
    artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
    if artists:
        for artist in artists:
            paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
            if paintings:
                for painting in paintings:
                    cprint(painting, "green")
            else:
                cprint(f"No {movement.name} paintings found", "green")
    else:
        cprint(f"No {movement.name} paintings found", "green")

# def list_movements_by_year():
#     movements = sorted(Movement.get_all(), key=lambda x: x.year_founded)
#     for movement in movements:
#         cprint(movement, "green")