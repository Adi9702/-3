
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt


class ClickCounter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Счётчик кликов")
        self.setFixedSize(300, 200)

        self.count = 0

        self.label = QLabel(f"Количество кликов: {self.count}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Нажми меня")
        self.button.clicked.connect(self.increase_count)
        # это чтобы при нажатии на кнопки увеличивался счётчик

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def increase_count(self):
        self.count += 1
        self.label.setText(f"Счётчик: {self.count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickCounter()
    window.show()
    sys.exit(app.exec())