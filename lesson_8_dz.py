
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)


class ShoppingListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping List by Geeks")
        self.setFixedSize(400, 300)

        self.init_ui()

    def init_ui(self):
        input_layout = QHBoxLayout()
        self.item_input = QLineEdit()
        self.item_input.setPlaceholderText("Введите название покупки...")
        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_item)

        input_layout.addWidget(self.item_input)
        input_layout.addWidget(self.add_button)
      
        self.item_list = QListWidget()

        self.delete_button = QPushButton("Удалить выбранное")
        self.delete_button.clicked.connect(self.delete_selected_item)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.item_list)
        main_layout.addWidget(self.delete_button)

        self.setLayout(main_layout)

    def add_item(self):
        "Добавление покупки"
        text = self.item_input.text().strip()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите название покупки")
            return

        self.item_list.addItem(text)
        self.item_input.clear()

    def delete_selected_item(self):
        "Удаление выбранной покупки"
        current_item = self.item_list.currentItem()
        if current_item:
            self.item_list.takeItem(self.item_list.row(current_item))
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите элемент для удаления")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingListApp()
    window.show()
    sys.exit(app.exec())