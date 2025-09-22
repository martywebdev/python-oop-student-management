from database.database import Database
import bcrypt


class Seeder:
    def __init__(self, db: Database = None):
        self.db = db or Database()

    def seed_users(self):
        # make sure users table exists
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)

        # check if users exist
        cursor = self.db.execute("SELECT COUNT(*) as count FROM users")
        row = cursor.fetchone()

        if row and row["count"] == 0:
            username = "admin"
            password = "admin123"
            password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

            self.db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
            print(f"✅ Seeded default user: {username}/{password}")
        else:
            print("ℹ️ Users already exist. Skipping seeding.")
