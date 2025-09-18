from database.database import Database
from model.student import Student


class StudentController:

    def __init__(self, db: Database = None):
        self.db = db or Database()

    def index(self):
        cursor = self.db.execute("SELECT * FROM students")
        # return list of Student objects
        return [Student(*row[1:4]) for row in cursor.fetchall()]

    def store(self, student: Student):
        query = "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)"
        self.db.execute(query, (student.name, student.course, student.mobile))

    def search(self, keyword: str):
        query = "SELECT * FROM students WHERE name LIKE ?"
        cursor = self.db.execute(query, (f"%{keyword}%",))
        return [Student(*row[1:4]) for row in cursor.fetchall()]

if __name__ == "__main__":
    controller = StudentController()
    students = controller.index()
    print(students)
