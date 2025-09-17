from database.database import Database


class StudentController:

    def __init__(self, db: Database = None):
        self.db = db or Database()

    def index(self):
        cursor = self.db.execute("SELECT * FROM students")
        return cursor.fetchall()


if __name__ == "__main__":
    controller = StudentController()
    students = controller.index()
    print(students)