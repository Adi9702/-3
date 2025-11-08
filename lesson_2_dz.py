
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout 
# здесь мы от библиотеки PyQt6 импортировали эти классы

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # здесь вызвали конструктор родительского класса. QWidget этот кдасс уже находится в библиотеке
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Введите тест:")
        self.line = QLineEdit()
        self.button = QPushButton("Нажмите кнопку")
        self.button.clicked.connect(self.on_click) 
        # тут написали что когда пользователь нажмет на кнопку вызовится функция "on_click"

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        text = self.line.text() 
        self.label.setText(f"Вы ввели: {text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
if __name__ == "__main__":
    main()
