import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel
)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Aqui eu estou criando o componente que vai armazenar os elementos
        layout = QVBoxLayout()

        # criando os elementos que seram inseridos no layout
        self.text_input = QLineEdit("Digite seu nome...")
        self.button = QPushButton("Clique aqui")
        self.label = QLabel("Bem-vindo!")

        # inserindo os elementos no layout
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        nome = self.text_input.text()
        self.label.setText(f"Olá, {nome}")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())