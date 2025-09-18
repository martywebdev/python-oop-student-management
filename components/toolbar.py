from PyQt6.QtWidgets import QToolBar


class Toolbar(QToolBar):
    
    def __init__(self):
        super().__init__()
        self.setMovable(True)
        