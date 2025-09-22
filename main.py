import sys
from PyQt6.QtWidgets import QApplication, QDialog

from controller.student_controller import StudentController
from controller.authentication_controller import AuthController
from views.student.main import StudentWindow
from views.auth.login import LoginDialog
from database.seeder import Seeder


def main():
    app = QApplication(sys.argv)

    # Run seeder (creates tables + default user if needed)
    Seeder().seed()

    # auth flow
    auth = AuthController()
    login = LoginDialog(auth)

    if login.exec() == QDialog.DialogCode.Accepted and login.success:
        controller = StudentController()
        student_view = StudentWindow(controller)
        student_view.show()
        sys.exit(app.exec())
    else:
        print("Login failed or cancelled")
        sys.exit(0)


if __name__ == "__main__":
    main()
