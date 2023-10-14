# lib/models/artist.py
from models.__init__ import CURSOR, CONN
from models.movement import Movement

class Artist():

    all = {}

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
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY,
            name TEXT,
            movement_id INTEGER,
            FOREIGN KEY (movement_id) REFERENCES movements(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS artists;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, movement_id):
        artist = cls(name, movement_id)
        artist.save()
        return artist

    def save(self):
        sql = """
            INSERT INTO artists (name, movement_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.movement_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self