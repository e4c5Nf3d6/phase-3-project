# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.movement import Movement
from models.painting import Painting

from helpers.helpers import spacer

def list_movements():
    spacer()
    movements = sorted(Movement.get_all(), key=lambda x: x.name.lower())
    for movement in movements:
        cprint(f"{movements.index(movement) + 1}. {movement.name}", "green")
    spacer()

def choose_movement():
    spacer()
    movements = sorted(Movement.get_all(), key=lambda x: x.name.lower())
    for movement in movements:
        print(f"{movements.index(movement) + 1}. {movement.name}")
    spacer()
    id = input("Enter the movement's ID: ")
    movements = sorted(Movement.get_all(), key=lambda x: x.name.lower())
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
    spacer()
    try:
        movement = Movement.create(name, year_founded)
        cprint(f'{movement.name} movement successfully created', "green")
    except Exception as exc:
        cprint(f"Error creating movement: {exc}", "red")

def update_movement(movement):
    try:
        name = input("Enter the movement's new name: ")
        movement.name = name
        year_founded = input("Enter the movement's new founding year: ")
        movement.year_founded = year_founded

        movement.update()
        spacer()
        cprint(f"{movement.name} movement successfully updated", "green")
    except Exception as exc:
        spacer()
        cprint(f"Error updating movement: {exc}", "red")

def delete_movement(movement):
    confirmation_text = colored(
        "Deleting a movement will delete all associated artists and paintings. Are you sure you want to proceed? Y/N: ", 
        "red", 
        attrs=["bold"]
    )
    spacer()
    confirmation = input(confirmation_text)
    spacer()
    if confirmation == "y" or confirmation == "Y":
        artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
        for artist in artists:
            paintings = [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
            for painting in paintings:
                painting.delete()
            artist.delete()
        movement.delete()
        cprint(f'{movement.name} movement successfully deleted', "green")
        return("deleted")
    else:
        cprint("Deletion aborted", "green")

def list_artists_by_movement(movement):
    artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
    spacer()
    if artists:
        for artist in artists:
            cprint(artist.name, "green")
    else:
        cprint(f'No {movement.name} artists found', "red")

def list_paintings_by_movement(movement):
    artists = [artist for artist in Artist.get_all() if artist.movement_id == movement.id]
    if artists:
        paintings = []
        for artist in artists:
            paintings = paintings + [painting for painting in Painting.get_all() if painting.artist_id == artist.id]
        if paintings:
            spacer()
            for painting in paintings:
                cprint(f"{painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")
            spacer()
        else:
            spacer()
            cprint(f"No {movement.name} paintings found", "green")
    else:
        cprint(f"No {movement.name} paintings found", "green")

# def list_movements_by_year():
#     movements = sorted(Movement.get_all(), key=lambda x: x.year_founded)
#     for movement in movements:
#         cprint(movement, "green")