# lib/models/movement.py
from models.__init__ import CURSOR, CONN

class Movement():

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Movement {self.id}: {self.name}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter    
    def name(self, name):
        if isinstance(name, str):
            self._name = name
