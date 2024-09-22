import sys
from PySide6.QtWidgets import QApplication, QLabel
"""
    Resumo geral:
        Criamos uma aplicação PySide (QApplication).
        Definimos um widget (no caso, um rótulo QLabel com texto).
        Tornamos esse widget visível com label.show().
        Iniciamos o loop de eventos para manter a aplicação rodando até que o usuário a feche.
"""
app = QApplication(sys.argv)

label = QLabel("Olá, Pyside")
label.show()

sys.exit(app.exec())