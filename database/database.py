import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('data/database.db')
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def close(self):
        self.connection.close()
