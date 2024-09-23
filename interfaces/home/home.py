from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)
from PySide6.QtCore import Qt

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Bem-vindo ao sistema!"))
        self.showMaximized()
        self.setLayout(layout)
