# lib/helpers.py

from termcolor import colored, cprint

from models.artist import Artist
from models.movement import Movement
from models.painting import Painting

from helpers.general_helpers import spacer

def list_movements():
    movements = sorted(Movement.get_all(), key=lambda x: x.name.lower())
    for movement in movements:
        cprint(f"{movements.index(movement) + 1}. {movement.name}", "green")

def choose_movement(prompt="Choose a movement: "):
    movements = sorted(Movement.get_all(), key=lambda x: x.name.lower())
    if movements:
        for movement in movements:
            print(f"{movements.index(movement) + 1}. {movement.name}")
        spacer()
        id = input(prompt)
        try:
            if int(id) == 0:
                raise ValueError
            return movements[int(id) - 1]
        except:
            spacer()
            cprint("Invalid choice", "red")
    else:
        spacer()
        cprint("No movements found", "red")

def create_movement():
    name = input("Enter the movement's name: ")
    year_founded = input("Enter the movement's founding year: ")
    spacer()
    try:
        movement = Movement.create(name, year_founded)
        cprint(f'{movement.name} movement successfully created', "green")
        return movement
    except Exception as exc:
        cprint(f"Error creating movement: {exc}", "red")
        return None

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
        "yellow", 
        attrs=["bold"]
    )
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
    artists = sorted(Artist.find_by_movement(movement.id), key=lambda x: x.name.lower())
    if artists:
        for artist in artists:
            cprint(artist.name, "green")
    else:
        cprint(f'No {movement.name} artists found', "red")
