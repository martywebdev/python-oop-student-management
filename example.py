# pylint: disable=E0611

import sys
from PyQt6.QtWidgets import (QApplication,
                             QPushButton,
                             QLabel,
                             QWidget,
                             QGridLayout,
                             QLineEdit)
from datetime import date, datetime


class AgeCalculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Age Calculator')
        grid = QGridLayout()

        # Widgets
        name_label = QLabel('Name:')
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel('Date of Birth MM/DD/YYYY:')
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")
        # Add widgets to the grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)  # this is QWidget method

    def calculate_age(self):
        dob_text = self.date_birth_line_edit.text().strip()

        try:
            # Validate format
            dob = datetime.strptime(dob_text, "%m/%d/%Y")
        except ValueError:
            self.output_label.setText("❌ Invalid date format! Use MM/DD/YYYY")
            return

        today = datetime.today()
        age = today.year - dob.year - \
            ((today.month, today.day) < (dob.month, dob.day))

        # this boolean that can be used in the equation
        print(((today.month, today.day) < (dob.month, dob.day)))

        name = self.name_line_edit.text().strip() or "User"
        self.output_label.setText(f"✅ {name}, you are {age} years old.")


app = QApplication(sys.argv)

age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
