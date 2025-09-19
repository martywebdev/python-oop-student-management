from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QMainWindow,
    QTableWidgetItem,
    QLabel
)

from PyQt6.QtGui import QAction, QIcon
from components.alert import Alert
from components.box_layout import BoxLayout
from components.dialog import Dialog
from components.select import Select
from components.statusbar import StatusBar
from components.table import Table

from components.toolbar import Toolbar
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

        add_student_action = QAction(
            QIcon("resources/icons/download.png"), "Add Student", self)
        add_student_action.triggered.connect(self.store)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

        search_action = QAction(
            QIcon("resources/icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        search_menu_item.addAction(search_action)

        # table
        self.table = Table(('Id', 'Name', 'Course', 'Mobile'))
        self.setCentralWidget(self.table)
        self.index()

        # toolbar
        toolbar = Toolbar()
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # status bar
        status_bar = StatusBar()
        self.setStatusBar(status_bar)

        # detect a cell click
        # self.table.cellClicked.connect(self.show)

    def index(self):
        students = self.controller.index()
        self.populate_table(students)

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
        dialog = Dialog('Add Student')

        search_text = QLineEdit()
        search_text.setPlaceholderText("Search")
        button = QPushButton('Search')
        reset_button = QPushButton("Reset")

        def handle_search():
            keyword = search_text.text()
            if keyword.strip():
                results = self.controller.search(keyword)
                if results:
                    self.populate_table(results)
                else:
                    Alert.info(self, "No students found matching your search")
                dialog.accept()  # closing dialog

        def handle_reset():
            self.populate_table(self.controller.index())
            dialog.accept()
            # close dialog
        button.clicked.connect(handle_search)
        reset_button.clicked.connect(handle_reset)

        layout = BoxLayout(
            search_text,
            button,
            reset_button
        )
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        dialog.setLayout(layout)
        dialog.exec()

    def populate_table(self, students):
        self.table.setRowCount(len(students))
        for row_number, student in enumerate(students):
            self.table.setItem(row_number, 0, QTableWidgetItem(
                str(row_number+1)))  # fake ID
            self.table.setItem(row_number, 1, QTableWidgetItem(student.name))
            self.table.setItem(row_number, 2, QTableWidgetItem(student.course))
            self.table.setItem(
                row_number, 3, QTableWidgetItem(str(student.mobile)))

    def show(self):
        pass
