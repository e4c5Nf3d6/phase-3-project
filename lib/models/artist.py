# lib/models/artist.py
from models.__init__ import CURSOR, CONN

class Artist():
    def __init__(self, name, movement_id, id=None):
        self.id = id
        self.name = name
        self.movement = movement_id

    def __repr__(self):
        return f"<Artist {self.id}: {self.name}, {self.movement}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("name must be a non-empty string")
        