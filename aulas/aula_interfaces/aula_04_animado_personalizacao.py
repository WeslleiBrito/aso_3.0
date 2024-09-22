from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Layout aninhado
        button_layout = QHBoxLayout()

        button1 = QPushButton("Botão 1")
        button2 = QPushButton("Botão 2")

        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        main_layout.addLayout(button_layout)

        # Aplicar estilo
        button1.setStyleSheet("background-color: red; color: white;")
        button2.setStyleSheet("background-color: blue; color: white;")

        # Definir layout principal
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
