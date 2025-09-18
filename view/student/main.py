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
from components.box_layout import BoxLayout
from components.dialog import Dialog
from components.select import Select
from components.table import Table

from model.student import Student

class StudentWindow(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Studend Management System")
        self.setMinimumSize(800, 600)
        # menubar

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        search_menu_item = self.menuBar().addMenu("&Search")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.store)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

        search_action = QAction("Search", self)
        search_action.triggered.connect(self.search)
        search_menu_item.addAction(search_action)

        # table
        self.table = Table(('Id', 'Name', 'Course', 'Mobile'))
        self.setCentralWidget(self.table)
        self.index()

    def index(self):
        students = self.controller.index()
        print("DEBUG students:", students)
        self.table.setRowCount(len(students))
        for row_idx, row in enumerate(students):
            for col_idx, value in enumerate(row):
                self.table.setItem(
                    row_idx, col_idx, QTableWidgetItem(str(value)))

    def store(self):
        dialog = Dialog('Add Student')

        student_name = QLineEdit()
        student_name.setPlaceholderText("name")

        courses = Select(['Computer Science', 'Accounting', "Cosmetology"])

        button = QPushButton('Register')

        def handle_register():

            name = student_name.text()
            course = courses.currentText()
            phone = mobile.text()

            if name.strip():
                student = Student(name, course, phone)   # wrap data into model
                self.controller.store(student)           # pass model
                self.index()
                dialog.accept()
                
        button.clicked.connect(handle_register)

        mobile = QLineEdit()
        mobile.setPlaceholderText("Mobile")

        layout = BoxLayout(
            student_name,
            courses,
            mobile,
            button
        )
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        dialog.setLayout(layout)
        dialog.adjustSize()
        # For modal dialog:
        dialog.exec()

    def search(self):
        pass
