from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pages._const import SIZE
from pages.admin_window import AdminWindow
from pages.exceptions.error_dialog import ErrorException


class Auth(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)
        self.size = QSize(SIZE['SMALLER'][0], SIZE['SMALLER'][1])
        self.setFixedSize(self.size)
        self.setWindowTitle('Login window')

        self.login_label = QLabel(self)
        self.password_label = QLabel(self)
        self.login = QLineEdit(self)
        self.button = QPushButton('Войти', self)

        self.error_input = ErrorException(text="Неверный логин или пароль", title="Неверный логин или пароль")
        self.error_user = ErrorException(text="Пользователь не найден!", title="Пользователь не найден")

        self.draw()

    def draw(self):
        self.login_label.setText('login:')
        self.login_label.move(20, 20)

        self.login.move(80, 20)
        self.login.resize(200, 32)

        self.button.clicked.connect(self.on_click)
        self.button.resize(200, 32)
        self.button.move(80, 120)

        self.show()

    def on_click(self):
        if self.login.text() == 'admin':
            self.destroy()
            a = AdminWindow()
            self.window.append(a)
            a.show()
        else:
            er = ErrorException(text="Роль не найдена", title="Ошибка!")
            self.window.append(er)
            er.show()
