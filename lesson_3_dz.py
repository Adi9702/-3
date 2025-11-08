import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton
)
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Виджет")
        self.resize(300, 150)

        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Введите текст:", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # это выравнивание текста по центру вот это (self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # QLabel - это поле для теста

        self.line_edit = QLineEdit(self)
        # QLineEdit - это поле ввода теста
        self.line_edit.setPlaceholderText("Текст...")

        self.btn_show = QPushButton("Показать текст", self)
        self.btn_exit = QPushButton("Закрыть", self)
        # QPushButton - это кнопка 

        self.btn_show.clicked.connect(self.show_text)
        self.btn_exit.clicked.connect(self.close_app)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.btn_show)
        layout.addWidget(self.btn_exit)
        # QVBoxLayout - это вертикальное расположение элементов

        central = QWidget(self)
        central.setLayout(layout)
        self.setCentralWidget(central)
        # QWidget - это виджет/окно

    def show_text(self):
        text = self.line_edit.text()
        if text.strip():
            self.label.setText(text)
        else:
            self.label.setText("Поле ввода пустое!")

    def close_app(self):
        QApplication.quit()
        # QAppLication - это управлением всем приложением


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()