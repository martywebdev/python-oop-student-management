from database.database import Database
from model.student import Student


class StudentController:
    def __init__(self, db: Database = None):
        self.db = db or Database()

    def index(self):
        cursor = self.db.execute("SELECT * FROM students")
        return [Student(row["id"], row["name"], row["course"], row["mobile"]) for row in cursor.fetchall()]

    def store(self, student: Student):
        query = "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)"
        self.db.execute(query, (student.name, student.course, student.mobile))

    def search(self, keyword: str):
        query = "SELECT * FROM students WHERE name LIKE ?"
        cursor = self.db.execute(query, (f"%{keyword}%",))
        return [Student(row["id"], row["name"], row["course"], row["mobile"]) for row in cursor.fetchall()]

    def show(self, student_id: int):
        query = "SELECT * FROM students WHERE id = ?"
        cursor = self.db.execute(query, (student_id,))
        row = cursor.fetchone()
        return Student(row["id"], row["name"], row["course"], row["mobile"]) if row else None

    def update(self, student_id: int, student: Student):
        query = "UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?"
        self.db.execute(query, (student.name, student.course,
                        student.mobile, student_id))

    def delete(self, student_id: int):
        query = "DELETE FROM students WHERE id = ?"
        self.db.execute(query, (student_id,))
