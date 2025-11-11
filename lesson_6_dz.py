import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List by Geeks")
        self.resize(400, 300)

        self.init_ui()

    def init_ui(self):
       
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введите новую задачу")

        self.btn_add = QPushButton("Добавить")
        self.btn_add.clicked.connect(self.add_task)

        # это список задач
        self.list_widget = QListWidget()

        self.delete_button = QPushButton("Удалить выбранное")
        self.delete_button.clicked.connect(self.delete_selected_item)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_task(self):
        "Добавление задачи"
        text = self.line_edit.text().strip()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите текст задачи")
            return
        self.list_widget.addItem(text)
        self.line_edit.clear()
        # эта функция чтобы добавить задачу в список, если поле не пустое

    def delete_selected_item(self):
        "Удаление выбранной задачи"
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            self.list_widget.takeItem(current_row)
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления")

        # эта функция чтобы удалить выбранную задачу из списка


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
