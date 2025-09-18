
import sys

from PyQt6.QtWidgets import (
    QApplication
)

from controller.student_controller import StudentController
from views.student.main import  StudentWindow


app = QApplication(sys.argv)
controller = StudentController()
student_view = StudentWindow(controller)
student_view.show()
sys.exit(app.exec())
