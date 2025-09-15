import sys
from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QApplication, QLabel, QLineEdit, QPushButton,
    QComboBox)


class AverageSpeedCalculator(QWidget):

    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        distance = QLabel("Distance")
        self.distance_value = QLineEdit()
        time_label = QLabel("Time (hours)")
        self.time_value = QLineEdit()

        button = QPushButton("Submit")
        button.clicked.connect(self.calculate)

        self.combo = QComboBox()
        self.combo.addItems(['Metric', 'Imperial'])

        self.result = QLabel("")

        grid.addWidget(distance, 0, 0)
        grid.addWidget(self.distance_value, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_value, 1, 1)
        grid.addWidget(button, 2, 1)

        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(self.result, 3, 0)
        self.setLayout(grid)

    def calculate(self):

        try:
            distance = float(self.distance_value.text())
            time = float(self.time_value.text())
            if time == 0:
                self.result.setText("❌ Time cannot be zero.")
                return

            avg_speed = distance / time

            if self.combo.currentText().startswith("Imperial"):
                avg_speed *= 0.621371  # convert km/h → mph
                self.result.setText(f"✅ Average speed: {avg_speed:.2f} mph")
            else:
                self.result.setText(f"✅ Average speed: {avg_speed:.2f} km/h")

        except ValueError:
            self.result.setText("❌ Enter valid numbers.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    average_speed_calc = AverageSpeedCalculator()
    average_speed_calc.show()
    app.exec()
