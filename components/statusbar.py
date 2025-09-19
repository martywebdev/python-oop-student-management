from PyQt6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):

    def __init__(self, *widgets):
        super().__init__()
        for widget in widgets:
            self.addWidget(widget)
