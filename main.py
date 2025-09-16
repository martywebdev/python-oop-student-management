import sqlite3
import sys
from tkinter import dialog

from PyQt6.QtWidgets import (
    QApplication, QPushButton, QLabel,
    QWidget, QComboBox, QGridLayout,
    QLineEdit,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QVBoxLayout
)

from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Studend Management System")

        # menubar

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

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
        self.table.setRowCount(0) # resetter
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


app = QApplication(sys.argv)
main = MainWindow()
main.load_data()
main.show()
sys.exit(app.exec())
