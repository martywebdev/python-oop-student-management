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


class Student(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Studend Management System")

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
        self.table = QTableWidget()  # central widget
        self.table.setFixedWidth(600)
        self.table.setFixedHeight(600)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)  # hide index
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
        pass

    def search(self):
        pass
