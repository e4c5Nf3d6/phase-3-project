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
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError('name must be a non-empty string')
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movements (
            id INTEGER PRIMARY KEY,
            name TEXT)
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
        if Movement.find_by_name(name):
            raise ValueError(f"This movement already exists: {Movement.find_by_name(name)}")
        else:
            movement = cls(name)
            movement.save()
            return movement

    def save(self):
        sql = """
            INSERT INTO movements (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        if Movement.find_by_name(self.name) and not Movement.find_by_name(self.name).id == self.id:
            raise ValueError(f"This movement already exists: {Movement.find_by_name(self.name)}")
        else:
            sql = """
                UPDATE movements
                SET name = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.id))
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
        else:
            movement = cls(row[1])
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