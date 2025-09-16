import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem
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
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

        # table
        self.table = QTableWidget()  # central widget
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False) # hide index 
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect('database.db')
        result = connection.execute('SELECT * FROM students')
        print(result)
        # populate the table
        # self.table.setRowCount(0) # resetter
        for row_number, row_data in enumerate(result): # this is the list
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data): # this is tuples inside the list
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

app = QApplication(sys.argv)
main = MainWindow()
main.load_data()
main.show()
sys.exit(app.exec())
