# lib/models/movement.py
from models.__init__ import CURSOR, CONN

class Movement():

    all = {}

    def __init__(self, name, year_founded, id=None):
        self.id = id
        self.name = name
        self.year_founded = year_founded

    def __repr__(self):
        return f"<Movement {self.id}: {self.name}, {self.year_founded}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter    
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError('name must be a non-empty string')
        
    @property
    def year_founded(self):
        return self._year_founded
    
    @year_founded.setter
    def year_founded(self, year):
        try:
            if isinstance(int(year), int) and 0 <= int(year) <= 2023:
                self._year_founded = int(year)
            else:
                raise ValueError
        except ValueError:
            raise ValueError("year_founded must be an integer between 0 and 2023")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movements (
            id INTEGER PRIMARY KEY,
            name TEXT,
            year_founded INTEGER)
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
    def create(cls, name, year_founded):
        if Movement.find_by_name(name):
            raise ValueError(f"This movement already exists")
        else:
            movement = cls(name, year_founded)
            movement.save()
            return movement

    def save(self):
        sql = """
            INSERT INTO movements (name, year_founded)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.year_founded))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE movements
            SET name = ?, year_founded = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.year_founded, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM movements
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        movement = cls.all.get(row[0])
        if movement:
            movement.name = row[1]
            movement.year_founded = row[2]
        else:
            movement = cls(row[1], row[2])
            movement.id = row[0]
            cls.all[movement.id] = movement
        return movement

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM movements
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM movements
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM movements
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None