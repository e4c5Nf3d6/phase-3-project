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

def find_artist_by_name():
    name = input("Enter the artist's name: ")
    artist = Artist.find_by_name(name)
    print(artist) if artist else print(f'Artist {name} not found')

def find_artist_by_id():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    print(artist) if artist else print(f'Artist {id_} not found')

def list_paintings():
    paintings = Painting.get_all()
    for painting in paintings:
        print(painting)

def find_painting_by_name():
    name = input("Enter the painting's name: ")
    painting = Painting.find_by_name(name)
    print(painting) if painting else print(f'Painting {name} not found')

def find_painting_by_id():
    id_ = input("Enter the painting's id: ")
    painting = Painting.find_by_id(id_)
    print(painting) if painting else print(f'Painting {id_} not found')

def list_movements():
    movements = Movement.get_all()
    for movement in movements:
        print(movement)

def find_movement_by_name():
    name = input("Enter the movement's name: ")
    movement = Movement.find_by_name(name)
    print(movement) if movement else print(f'Movement {name} not found')

def find_movement_by_id():
    id_ = input("Enter the movement's id: ")
    movement = Movement.find_by_id(id_)
    print(movement) if movement else print(f'Movement {id_} not found')
