# lib/helpers.py

from models.artist import Artist
from models.movement import Movement
from models.painting import Painting

def exit_program():
    print("Goodbye!")
    exit()

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(artist)

def list_paintings():
    paintings = Painting.get_all()
    for painting in paintings:
        print(painting)

def list_movements():
    movements = Movement.get_all()
    for movement in movements:
        print(movement)
