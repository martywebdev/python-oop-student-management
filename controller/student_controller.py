from database.database import Database
from model.student import Student


class StudentController:

    def __init__(self, db: Database = None):
        self.db = db or Database()

    def index(self):
        cursor = self.db.execute("SELECT * FROM students")
        return cursor.fetchall()

    def store(self, student: Student):
        query = "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)"
        self.db.execute(query, (student.name, student.course, student.mobile))


if __name__ == "__main__":
    controller = StudentController()
    students = controller.index()
    print(students)
