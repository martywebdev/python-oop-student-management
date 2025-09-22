from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel
from components.box_layout import BoxLayout
from components.alert import Alert


class LoginDialog(QDialog):
    def __init__(self, auth_controller):
        super().__init__()
        self.setWindowTitle("Login")
        self.auth_controller = auth_controller
        self.success = False

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText("Password")

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)

        layout = BoxLayout(
            QLabel("Username"), self.username,
            QLabel("Password"), self.password,
            login_button
        )
        self.setLayout(layout)
        self.adjustSize()

    def handle_login(self):
        if self.auth_controller.login(self.username.text(), self.password.text()):
            self.success = True
            self.accept()
        else:
            Alert.error(self, "Invalid username or password")
