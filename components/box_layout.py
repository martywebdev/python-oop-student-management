from PyQt6.QtWidgets import QVBoxLayout

class BoxLayout(QVBoxLayout):
    
    def __init__(self, *widgets):
        super().__init__()
        for widget in widgets:
            self.addWidget(widget)