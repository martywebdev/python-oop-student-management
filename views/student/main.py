from PyQt6.QtWidgets import (
    QPushButton,
    QLineEdit,
    QMainWindow,
    QTableWidgetItem,
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
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        # menubar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        search_menu_item = self.menuBar().addMenu("&Search")

        add_student_action = QAction(
            QIcon("resources/icons/download.png"), "Add Student", self
        )
        add_student_action.triggered.connect(self.store)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        search_action = QAction(
            QIcon("resources/icons/search.png"), "Search", self
        )
        search_action.triggered.connect(self.search)
        search_menu_item.addAction(search_action)

        # table
        self.table = Table(("Id", "Name", "Course", "Mobile"))
        self.setCentralWidget(self.table)
        self.index()

        # toolbar
        toolbar = Toolbar()
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # status bar
        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)

        # detect a cell click
        self.selected_id = None
        self.table.cellClicked.connect(self.selected)

        self.edit_button = QPushButton("Edit Record")
        self.status_bar.addWidget(self.edit_button)
        self.edit_button.clicked.connect(self.edit)
        self.edit_button.setEnabled(False)

        self.delete_button = QPushButton("Delete Record")
        self.status_bar.addWidget(self.delete_button)
        self.delete_button.clicked.connect(self.delete)
        self.delete_button.setEnabled(False)

    def index(self):
        students = self.controller.index()
        self.populate_table(students)

    def store(self):
        dialog = Dialog("Add Student")

        student_name = QLineEdit()
        student_name.setPlaceholderText("Name")

        courses = Select(["Computer Science", "Accounting", "Cosmetology"])

        mobile = QLineEdit()
        mobile.setPlaceholderText("Mobile")

        button = QPushButton("Register")

        def handle_register():
            name = student_name.text().strip()
            course = courses.currentText()
            phone = mobile.text().strip()

            if name:
                student = Student(None, name, course, phone)
                self.controller.store(student)
                self.index()
                dialog.accept()

        button.clicked.connect(handle_register)

        layout = BoxLayout(student_name, courses, mobile, button)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        dialog.setLayout(layout)
        dialog.adjustSize()
        dialog.exec()

    def search(self):
        dialog = Dialog("Search Student")

        search_text = QLineEdit()
        search_text.setPlaceholderText("Search")
        button = QPushButton("Search")
        reset_button = QPushButton("Reset")

        def handle_search():
            keyword = search_text.text()
            if keyword.strip():
                results = self.controller.search(keyword)
                if results:
                    self.populate_table(results)
                else:
                    Alert.info(self, "No students found matching your search")
                dialog.accept()

        def handle_reset():
            self.populate_table(self.controller.index())
            dialog.accept()

        button.clicked.connect(handle_search)
        reset_button.clicked.connect(handle_reset)

        layout = BoxLayout(search_text, button, reset_button)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        dialog.setLayout(layout)
        dialog.exec()

    def populate_table(self, students):
        self.table.setRowCount(len(students))
        for row_number, student in enumerate(students):
            self.table.setItem(
                row_number, 0, QTableWidgetItem(str(student.id)))
            self.table.setItem(row_number, 1, QTableWidgetItem(student.name))
            self.table.setItem(row_number, 2, QTableWidgetItem(student.course))
            self.table.setItem(
                row_number, 3, QTableWidgetItem(str(student.mobile)))

    def selected(self, row, column):
        self.selected_id = int(self.table.item(row, 0).text())
        self.edit_button.setEnabled(True)
        self.delete_button.setEnabled(True)

    def edit(self):
        student = self.controller.show(self.selected_id)
        if not student:
            Alert.error(self, "Student not found")
            return

        dialog = Dialog(f"Edit Student - {student.name}")

        student_name = QLineEdit(student.name)
        courses = Select(["Computer Science", "Accounting", "Cosmetology"])
        courses.setCurrentText(student.course)
        mobile = QLineEdit(str(student.mobile))

        button = QPushButton("Save Changes")

        def handle_update():
            name = student_name.text().strip()
            course = courses.currentText()
            phone = mobile.text().strip()

            if name:
                updated_student = Student(student.id, name, course, phone)
                self.controller.update(student.id, updated_student)
                self.index()
                dialog.accept()

        button.clicked.connect(handle_update)

        layout = BoxLayout(student_name, courses, mobile, button)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        dialog.setLayout(layout)
        dialog.exec()

    def delete(self):
        if not self.selected_id:
            return

        confirm = Alert.confirm(self, f"Delete student ID {self.selected_id}?")
        if confirm:  # Alert.confirm should return True/False
            self.controller.delete(self.selected_id)
            self.index()  # refresh table
            self.selected_id = None
            self.edit_button.setEnabled(False)
            self.delete_button.setEnabled(False)
