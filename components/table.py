from PyQt6.QtWidgets import (
    QTableWidget, 
    QHeaderView
)


class Table(QTableWidget):

    def __init__(self, headers, width=600, height=600):

        super().__init__()
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        self.verticalHeader().setVisible(False)

        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
