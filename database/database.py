import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):

        env = os.getenv("APP_ENV", "dev")

        if env == "dev":
            self.db_path = Path("data/database.db")
        else:

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
