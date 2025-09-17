from calendar import c
import os
import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication, QPushButton, QLabel,
    QWidget, QComboBox, QGridLayout,
    QLineEdit,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QVBoxLayout,
)

from PyQt6.QtGui import QAction, QColor

from controller.student_controller import StudentController
from view.student.main import Student


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Studend Management System")

        # menubar

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        search_menu_item = self.menuBar().addMenu("&Search")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

        search_action = QAction("Search", self)
        search_action.triggered.connect(self.show_search_dialog)
        search_menu_item.addAction(search_action)

        # table
        self.table = QTableWidget()  # central widget
        self.table.setFixedWidth(600)
        self.table.setFixedHeight(600)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)  # hide index
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect('database.db')
        result = connection.execute('SELECT * FROM students')
        print(result)
        # populate the table
        self.table.setRowCount(0)  # resetter
        for row_number, row_data in enumerate(result):  # this is the list
            self.table.insertRow(row_number)
            # this is tuples inside the list
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number,
                                   QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def show_search_dialog(self):
        search_dialog = QDialog(self)
        search_dialog.setWindowTitle("Search Dialog")
        search_dialog.setFixedWidth(200)
        search_dialog.setFixedHeight(100)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Search"))
        search_input = QLineEdit()
        layout.addWidget(search_input)

        button = QPushButton('Submit')
        button.clicked.connect(lambda: self.search(search_input.text()))
        layout.addWidget(button)

        search_dialog.setLayout(layout)

        # For modal dialog:
        search_dialog.exec()

    def search(self, search_string):
        with sqlite3.connect("database.db") as conn:
            result = conn.execute(
                "SELECT * FROM students where name like ? ", (f"%{search_string}%",))
            rows = result.fetchall()

            print(rows)
            # reset all highlights first
            for row in range(self.table.rowCount()):
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    if item:
                        item.setBackground(QColor("white"))  # reset to default

            # highlight matches
               # highlight matches (starting with search_string)
            for row in range(self.table.rowCount()):
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    if item and item.text().lower().startswith(search_string.lower()):
                        # highlight the whole row
                        for c in range(self.table.columnCount()):
                            match_item = self.table.item(row, c)
                            if match_item:
                                match_item.setBackground(QColor("yellow"))
            # populate the table with search results

            # self.table.setRowCount(0)
            # for row_number, row_data in enumerate(rows):
            #     self.table.insertRow(row_number)
            #     for column_number, data in enumerate(row_data):
            #         self.table.setItem(
            #             row_number,
            #             column_number,
            #             QTableWidgetItem(str(data))
            #         )


class InsertDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Student')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # this is an inpput
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # this is a dropdown
        self.course_name = QComboBox()
        courses = ['Computer Science', 'Accounting', "Cosmetology"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # this is an inpput
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # submit button
        button = QPushButton('Register')
        button.clicked.connect(self.add_student)
        layout.addWidget(button)
        self.setLayout(layout)

    def add_student(self):

        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()

        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)', (name, course, mobile))
            conn.commit()
            main.load_data()


# app = QApplication(sys.argv)
# main = MainWindow()
# main.load_data()
# main.show()
# sys.exit(app.exec())
print(os.getcwd())
app = QApplication(sys.argv)
controller = StudentController()
student_view = Student(controller)
student_view.show()
sys.exit(app.exec())
