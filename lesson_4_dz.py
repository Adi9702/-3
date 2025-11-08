
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QSpinBox, QComboBox, QCheckBox, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QStatusBar
)
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Моя библиотека")
        self.resize(800, 500)

        central = QWidget(self)
        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        form = QFormLayout()

        self.name_input = QLineEdit()
        name = QRegularExpression(r"^[\p{L}\s\-]{2,40}$")
        self.name_input.setValidator(QRegularExpressionValidator(name))
        form.addRow("Название:", self.name_input)
        
        self.author_input = QLineEdit()
        author = QRegularExpression(r"^[\p{L}\s\-]{2,40}$")
        self.author_input.setValidator(QRegularExpressionValidator(author))
        form.addRow("Автор:", self.author_input)

        self.year_input = QSpinBox()
        self.year_input.setRange(1800, 2025)
        self.year_input.setValue(2023)
        self.year_input.valueChanged.connect(
            lambda v: self.status.showMessage(f"Год: {v}", 2000)
        )
        form.addRow("Год:", self.year_input)

        self.genre_input = QComboBox()
        self.genre_input.addItems(["Роман", "Детектив", "Фантастика"])
        form.addRow("Жанр:", self.genre_input)

        self.read_checkbox = QCheckBox("Прочитано")
        form.addRow("", self.read_checkbox)

        actions = QHBoxLayout()
        self.add_btn = QPushButton("Добавить")
        self.add_btn.clicked.connect(self.add_book)

        self.clear_btn = QPushButton("Очистить")
        self.clear_btn.clicked.connect(self.clear_form)

        self.exit_btn = QPushButton("Выход")
        self.exit_btn.clicked.connect(self.close)

        actions.addWidget(self.add_btn)
        actions.addWidget(self.clear_btn)
        actions.addWidget(self.exit_btn)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels([
            "Название", "Автор", "Год", "Жанр", "Прочитано"
        ])
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)

    
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        left_layout.addLayout(form)
        left_layout.addLayout(actions)
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.table)
        root.addLayout(main_layout)

    def add_book(self):
        name = self.name_input.text().strip()
        author = self.author_input.text().strip()
        year = str(self.year_input.value())
        genre = self.genre_input.currentText()
        read = "Да" if self.read_checkbox.isChecked() else "Нет"

        if not name or not author:
            QMessageBox.warning(self, "Ошибка", "Введите название и автора!")
            return

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(name))
        self.table.setItem(row_position, 1, QTableWidgetItem(author))
        self.table.setItem(row_position, 2, QTableWidgetItem(year))
        self.table.setItem(row_position, 3, QTableWidgetItem(genre))
        self.table.setItem(row_position, 4, QTableWidgetItem(read))

        self.status.showMessage(f"Добавлена книга: {name}", 3000)
        self.clear_form()

    def clear_form(self):
        self.name_input.clear()
        self.author_input.clear()
        self.year_input.setValue(2023)
        self.genre_input.setCurrentIndex(0)
        self.read_checkbox.setChecked(False)
        self.status.showMessage("Форма очищена", 2000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())