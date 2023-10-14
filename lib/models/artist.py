# lib/models/artist.py
from models.__init__ import CURSOR, CONN
from movement import Movement

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
        
    @property
    def movement_id(self):
        return self._movement_id

    @movement_id.setter
    def department_id(self, movement_id):
        if isinstance(movement_id, int) and Movement.find_by_id(movement_id):
            self._movement_id = movement_id
        else:
            raise ValueError("movement_id must reference a movement in the database")