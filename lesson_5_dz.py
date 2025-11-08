
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox
)
from PyQt6.QtCore import Qt


class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Конвертер валют")
        self.resize(400, 300)

        # Валюты
        self.rates = {
            'USD': 1,
            'EUR': 0.9,
            'KGS': 100
        }

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        self.amount_label = QLabel("Введите сумму:")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Например, 100")

        self.from_currency = QComboBox()
        self.from_currency.addItems(self.rates.keys())

        self.to_currency = QComboBox()
        self.to_currency.addItems(self.rates.keys())

        self.convert_button = QPushButton("Конвертировать")
        self.clear_button = QPushButton("Очистить")

        self.result_label = QLabel("Результат: —")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

       
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_label)
        amount_layout.addWidget(self.amount_input)

    
        currency_layout = QHBoxLayout()
        currency_layout.addWidget(QLabel("Из валюты:"))
        currency_layout.addWidget(self.from_currency)
        currency_layout.addWidget(QLabel("В валюту:"))
        currency_layout.addWidget(self.to_currency)

       
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.convert_button)
        button_layout.addWidget(self.clear_button)

     
        main_layout.addLayout(amount_layout)
        main_layout.addLayout(currency_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_label)

    
        self.convert_button.clicked.connect(self.convert_currency)
        self.clear_button.clicked.connect(self.clear_fields)


    def convert_currency(self):
        try:
            amount = float(self.amount_input.text().replace(",", "."))
        except ValueError:
            QMessageBox.warning(self, "Ошибка ввода", "Введите корректное числовое значение суммы.")
            return

        from_curr = self.from_currency.currentText()
        to_curr = self.to_currency.currentText()

    
        result = amount * (self.rates[to_curr] / self.rates[from_curr])
        self.result_label.setText(f"Результат: {result:.2f} {to_curr}")


    def clear_fields(self):
        self.amount_input.clear()
        self.from_currency.setCurrentIndex(0)
        self.to_currency.setCurrentIndex(0)
        self.result_label.setText("Результат: —")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec())