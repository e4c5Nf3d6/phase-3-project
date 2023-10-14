# lib/models/movement.py
from models.__init__ import CURSOR, CONN

class Movement():

    all = {}

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
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movements (
            id INTEGER PRIMARY KEY,
            name TEXT,
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movements;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name):
        movement = cls(name)
        movement.save()
        return movement

    def save(self):
        sql = """
                INSERT INTO movements (name)
                VALUES (?)
        """

        CURSOR.execute(sql, (self.name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
