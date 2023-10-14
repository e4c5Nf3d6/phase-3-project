# lib/models/artist.py
from models.__init__ import CURSOR, CONN

class Artist():
    def __init__(self, name, period, id=None):
        self.id = id
        self.name = name
        self.period = period

    def __repr__(self):
        return f"<Artist {self.id}: {self.name}, {self.period}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("name must be a non-empty string")
        