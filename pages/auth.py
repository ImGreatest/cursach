from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from data.role import RoleService
from data.user import UserService
from pages._const import SIZE, ROLES
from pages.admin_window import AdminWindow
from pages.cook_panel import CookPanel
from pages.exceptions.error_dialog import ErrorException
from pages.waiter_panel import WaiterPanel


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
        self.password = QLineEdit(self)
        self.button = QPushButton('Accept', self)

        self.error_input = ErrorException(text="Неверный логин или пароль", title="Неверный логин или пароль")
        self.error_user = ErrorException(text="Пользователь не найден!", title="Пользователь не найден")

        self.user_service = UserService()
        self.role_service = RoleService()

        self.draw()

    def __repr__(self):
        pass

    def draw(self):
        self.login_label.setText('login:')
        self.login_label.move(20, 20)

        self.login.move(80, 20)
        self.login.resize(200, 32)

        self.password_label.setText('password:')
        self.password_label.move(20, 67.5)

        self.password.move(80, 65)
        self.password.resize(200, 32)

        self.button.clicked.connect(self.on_click)
        self.button.resize(200, 32)
        self.button.move(80, 120)

        self.show()

    def validate(self):
        if len(self.login.text()) >= 1 or len(self.password.text()) >= 1:
            print(self.login.text(), self.password.text())
            user = self.user_service.get_by_name(self.login.text(), self.password.text())
            print('ssssssss', user)
            if user:
                role = self.role_service.get_by_id(user['role'])
                return role['name']
            else:
                e = ErrorException(text="Неверный логин или пароль", title="Ошибка!")
                self.window.append(e)
                e.show()
        else:
            er = ErrorException(text="Неверный логин или пароль", title="Ошибка!")
            self.window.append(er)
            er.show()

    def on_click(self):
        role = self.validate()
        print(role)
        if role == ROLES.get('admin'):
            self.destroy()
            a = AdminWindow()
            self.window.append(a)
            a.show()
        elif role == ROLES.get('cook'):
            self.destroy()
            c = CookPanel()
            self.window.append(c)
            c.show()
        elif role == ROLES.get('waiter'):
            self.destroy()
            w = WaiterPanel()
            self.window.append(w)
            w.show()
        else:
            er = ErrorException(text="Роль не найдена", title="Ошибка!")
            self.window.append(er)
            er.show()
