import sys
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit,
    QMainWindow)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Studend Management System")
        
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        
        


app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())
