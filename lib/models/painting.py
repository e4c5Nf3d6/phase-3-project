# lib/models/painting.py
import re
from models.__init__ import CURSOR, CONN
from artist import Artist

class Painting():

    all = {}
    mediums = ['acrylic', 'encaustic', 'fresco', 'oil', 'tempera', 'watercolor']

    def __init__(self, name, year, medium, artist_id, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.medium = medium
        self.artist_id = artist_id

    def __repr__(self):
        return (
            f"<Painting {self.id}: {self.name}, {self.year}, {self.medium}, " +
            f"Artist ID: {self.artist_id}>"
        )

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
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        pattern = re.compile("^[0-9]$|^[1-9][0-9]{1,3}$|^20[0-1][0-9]$|^202[0-3]$|^[1-9][0-9]{0,4}?\sBC$")
        if pattern.match(year):
            self._year = year
        else:
            raise ValueError("year must be a year between 99999 BC and 2023")
        
    @property
    def medium(self):
        return self._medium
    
    @medium.setter
    def medium(self, medium):
        if medium in Painting.mediums:
            self._medium = medium

    @property
    def artist_id(self):
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        if isinstance(artist_id, int) and Artist.find_by_id(artist_id):
            self._artist_id = artist_id
        else:
            raise ValueError("artist_id must reference a artist in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS paintings (
            id INTEGER PRIMARY KEY,
            name TEXT,
            year TEXT,
            medium TEXT,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS paintings;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO paintings (name, year, medium, artist_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.year, self.medium, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self