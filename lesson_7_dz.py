import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)
from PyQt6.QtCore import Qt


class ShoppingListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping List by Geeks")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите товар...")
        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_item)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.add_button)

        self.list_widget = QListWidget()

        self.delete_button = QPushButton("Удалить выбранное")
        self.delete_button.clicked.connect(self.delete_item)

        layout.addLayout(input_layout)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def add_item(self):
        text = self.input_field.text().strip()
        if text:
            self.list_widget.addItem(text)
            self.input_field.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Поле ввода не должно быть пустым!")

    def delete_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.list_widget.takeItem(self.list_widget.row(selected_item))
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите элемент для удаления!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingListApp()
    window.show()
    sys.exit(app.exec())