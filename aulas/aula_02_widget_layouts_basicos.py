import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # criar layout
        layout = QVBoxLayout()

        # criar widgets
        self.text_input = QLineEdit("Digite algo")
        self.button = QPushButton("Clique aqui")

        # Adicionando os itens ao layout
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)

        # configurar o layout
        self.setLayout(layout)


app = QApplication(sys.argv)

# instanciar a janela e exibir
window = MyWindow()
window.show()

sys.exit(app.exec())