# lib/models/artist.py
from models.__init__ import CURSOR, CONN
from models.movement import Movement

class Artist():

    all = {}

    def __init__(self, name, movement_id, id=None):
        self.id = id
        self.name = name
        self.movement_id = movement_id

    def __repr__(self):
        return (
            f"<Artist {self.id}: {self.name}, " + 
            f"Movement ID: {self.movement_id}>"
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
    def movement_id(self):
        return self._movement_id

    @movement_id.setter
    def movement_id(self, movement_id):
        try:
            if isinstance(int(movement_id), int) and Movement.find_by_id(int(movement_id)):
                self._movement_id = int(movement_id)
            else:
                raise ValueError
        except ValueError:
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

    def save(self):
        sql = """
            INSERT INTO artists (name, movement_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.movement_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE artists
            SET name = ?, movement_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.movement_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM artists
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, movement_id):
        artist = cls(name, movement_id)
        artist.save()
        return artist
    
    @classmethod
    def instance_from_db(cls, row):
        artist = cls.all.get(row[0])
        if artist:
            artist.name = row[1]
            artist.movement_id = row[2]
        else:
            artist = cls(row[1], row[2])
            artist.id = row[0]
            cls.all[artist.id] = artist
        return artist

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM artists
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM artists
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM artists
            WHERE name is ?
        """

        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None