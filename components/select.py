from PyQt6.QtWidgets import QComboBox

class Select(QComboBox):
    
    def __init__(self, *options):
        super().__init__()
        for option in options:
            if isinstance(option, (list, tuple)):
                self.addItems(option)
            else:
                self.addItem(option)
        