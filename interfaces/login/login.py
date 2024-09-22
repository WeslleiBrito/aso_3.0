import sys

from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QGridLayout
)
from PySide6.QtGui import (
    QPixmap
)


from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

import  locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

users = [
    {"id": 1, "name": "Wesllei"},
    {"id": 2, "name": "Antonio"},
    {"id": 3, "name": "Ravena"},
    {"id": 4, "name": "Andressa"},
    {"id": 5, "name": "Melissa"}
]

users = sorted(users, key=lambda user: user["name"])

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.__visible: bool = False

        self.setFixedSize(350, 420)
        self.setWindowTitle("Login")

        password_layout = QGridLayout()

        self.toggle_visibility_button = QPushButton()
        self.toggle_visibility_button.setIcon(QIcon(r"C:\Users\Wesllei Brito\PycharmProjects\aso_3.0\icons\visibility_off_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"))
        self.toggle_visibility_button.clicked.connect(self.on_set_visible)
        self.setWindowIcon(QIcon(
            r"C:\Users\Wesllei Brito\PycharmProjects\aso_3.0\icons\passkey_24dp_75FBFD_FILL0_wght400_GRAD0_opsz24.svg"))
        self.toggle_visibility_button.setFixedSize(QSize(24, 24))
        self.toggle_visibility_button.setStyleSheet("border: none; padding-right: 10px;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25,50,25, 40)

        self.image_logo = QLabel(self)
        logo = QPixmap(r"C:\Users\Wesllei Brito\PycharmProjects\aso_3.0\images\Blue_Flat_Illustrative_Human_Artificial_Intelligence_Technology_Logo-removebg-preview.png")
        self.image_logo.setPixmap(logo.scaled(130, 130))

        access_layout = QVBoxLayout()
        access_layout.setContentsMargins(0,20,0,0)
        self.combo_user = QComboBox()
        self.combo_user.setFixedSize(300, 40)
        self.combo_user.setStyleSheet("QComboBox { padding: 10px; font-weight: Bold; font-size: 14px}")

        for user in users:
            self.combo_user.addItem(user["name"], user["id"])

        self.combo_user.currentIndexChanged.connect(self.selected_user)

        self.password = QLineEdit()
        self.password.setFixedSize(300, 35)
        self.password.setPlaceholderText("Senha")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("QLineEdit { padding-left: 10px; font-weight: Bold; font-size: 14px}")
        password_layout.addWidget(self.password, 0, 0)
        password_layout.addWidget(self.toggle_visibility_button, 0, 1)

        button_layout = QHBoxLayout()

        button_enter = QPushButton("Entrar")
        button_cancel = QPushButton("Cancelar")

        button_layout.addWidget(button_enter, alignment=Qt.AlignmentFlag.AlignLeft)
        button_layout.addWidget(button_cancel)


        button_enter.setFixedSize(130, 40)
        button_cancel.setFixedSize(100, 40)

        access_layout.addWidget(self.combo_user)
        access_layout.addLayout(password_layout)
        access_layout.addLayout(button_layout)


        self.check_memorize = QCheckBox("Relembrar meu usuário?")
        self.check_memorize.stateChanged.connect(self.on_memorize)

        main_layout.addWidget(self.image_logo, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        main_layout.addLayout(access_layout)
        main_layout.addWidget(self.check_memorize, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        self.setLayout(main_layout)

    def selected_user(self):
        return self.combo_user.currentData()


    def on_memorize(self) -> int:
        if self.check_memorize.isChecked():
            return 1
        return 0

    def on_set_visible(self):
        if self.__visible:
            self.password.setEchoMode(QLineEdit.Password)
            self.toggle_visibility_button.setIcon(QIcon(r"C:\Users\Wesllei Brito\PycharmProjects\aso_3.0\icons\visibility_off_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"))
        else:
            self.password.setEchoMode(QLineEdit.Normal)
            self.toggle_visibility_button.setIcon(QIcon(
                r"C:\Users\Wesllei Brito\PycharmProjects\aso_3.0\icons\visibility_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"))
        self.__visible = not self.__visible


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(r"C:\Users\Wesllei Brito\PycharmProjects\aso_3.0\icons\acordo.ico"))
window = Login()

screen = app.primaryScreen()
screen_geometry = screen.geometry()

x = (screen_geometry.width() - window.width()) // 2
y = (screen_geometry.height() - window.height()) // 2

window.setGeometry(x, y, window.width(), window.height())
window.show()

sys.exit(app.exec())