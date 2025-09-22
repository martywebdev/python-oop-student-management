from database.database import Database
import bcrypt


class AuthController:
    def __init__(self, db: Database = None):
        self.db = db or Database()

    def register(self, username: str, password: str):
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        query = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        self.db.execute(query, (username, password_hash))

    def login(self, username: str, password: str) -> bool:
        query = "SELECT * FROM users WHERE username = ?"
        cursor = self.db.execute(query, (username,))
        row = cursor.fetchone()
        if row and bcrypt.checkpw(password.encode("utf-8"), row["password_hash"].encode("utf-8")):
            return True
        return False
