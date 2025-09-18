from PyQt6.QtWidgets import QDialog


class Dialog(QDialog):

    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)