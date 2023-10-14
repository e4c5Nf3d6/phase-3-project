# lib/models/painting.py
from models.__init__ import CURSOR, CONN

class Painting():
    def __init__(self, name, medium, artist_id, id=None):
        self.id = id
        self.name = name
        self.medium = medium
        self.artist_id = artist_id

    def __repr__(self):
        return (
            f"<Painting {self.id}: {self.name}, {self.medium}, " +
            f"Artist ID: {self.artist_id}>"
        )
