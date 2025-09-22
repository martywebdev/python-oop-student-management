import os
import sqlite3
from pathlib import Path


class Database:
    def __init__(self):
        # cross-platform app data directory
        app_dir = Path.home() / ".student_management"
        app_dir.mkdir(parents=True, exist_ok=True)

        self.db_path = app_dir / "database.db"

        # connect with row factory for dict-like access
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def close(self):
        self.connection.close()
