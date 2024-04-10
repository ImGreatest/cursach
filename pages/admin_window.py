from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from data.order import OrderService
from data.role import RoleService
from data.shift import ShiftService
from data.shift_user import ShiftUserService
from data.status import StatusService
from data.user import UserService
from pages.exceptions.error_dialog import ErrorException


class AdminWindow(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.user_service = UserService()
        self.role_service = RoleService()
        self.order_service = OrderService()
        self.status_service = StatusService()

        data_rows = []
        users = self.user_service.get()
        for user in users:
            data_rows.append(
                [user['id'], user['name'], self.role_service.get_by_id(user['role'])['name'], user['status']])

        self.size = QSize(940, 800)
        self.setFixedSize(self.size)
        self.setWindowTitle('Админская панель')

        # m_myWidget = QWidget(self)
        # m_myWidget.setGeometry(100, 100, 940, 700)
        # m_myWidget.setAttribute(Qt.WA_StyledBackground)
        # m_myWidget.setStyleSheet('background-color: red;')
        # m_myWidget.show()

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_create = QAction(QIcon('img/ui/new.png'), 'Смены', self)
        toolbar_button_create.setStatusTip('Смены')
        toolbar_button_create.setCheckable(True)
        toolbar_button_create.triggered.connect(self.call_shifts)
        toolbar.addAction(toolbar_button_create)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_delete = QAction(QIcon('img/ui/minus.png'), 'Уволить', self)
        toolbar_button_delete.setStatusTip('Уволить')
        toolbar_button_delete.setCheckable(True)
        toolbar_button_delete.triggered.connect(self.call_form_change_status)
        toolbar.addAction(toolbar_button_delete)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_delete_user = QAction(QIcon('img/ui/plus.png'), 'Создать пользователя', self)
        toolbar_button_delete_user.setStatusTip('Создать пользователя')
        toolbar_button_delete_user.setCheckable(True)
        toolbar_button_delete_user.triggered.connect(self.call_user_form)
        toolbar.addAction(toolbar_button_delete_user)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_delete_user = QAction(QIcon('img/ui/book-alt.png'), 'Заказы', self)
        toolbar_button_delete_user.setStatusTip('Заказы')
        toolbar_button_delete_user.setCheckable(True)
        toolbar_button_delete_user.triggered.connect(self.call_order_window)
        toolbar.addAction(toolbar_button_delete_user)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/refresh.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        central = QWidget(self)
        self.setCentralWidget(central)
        self.grid = QGridLayout(self)
        central.setLayout(self.grid)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(self.order_service.count_orders())
        self.table.setHorizontalHeaderLabels(['ID', 'Статус', 'Роль', 'Имя'])
        user = self.user_service.get()
        self.table.setRowCount(*self.user_service.count())
        for i, v in enumerate(user):
            self.table.setItem(i, 0, QTableWidgetItem(str(v['id'])))
            self.table.setItem(i, 1, QTableWidgetItem(str(v['status'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(self.role_service.get_by_id(v['role'])['name'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v['name'])))

        self.grid.addWidget(self.table, 0, 0)

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = AdminWindow()
            self.window.append(a)
            a.show()

    def call_order_window(self, state):
        if state:
            a = OrderWindow()
            self.window.append(a)
            a.show()

    def call_user_form(self, state):
        if state:
            a = FormCreateUser()
            self.window.append(a)
            a.show()

    def call_form_change_status(self, state):
        if state:
            a = FormChangeStatusAdmin()
            self.window.append(a)
            a.show()

    def call_shifts(self, state):
        if state:
            a = Shifts()
            self.window.append(a)
            a.show()


class FormChangeStatusAdmin(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.status_service = StatusService()
        self.user_service = UserService()
        self.role_service = RoleService()

        self.setMinimumSize(QSize(320, 180))
        self.setWindowTitle('Уволить')

        self.idLabel = QLabel(self)
        self.idLabel.setText('ID:')
        self.idLabel.move(20, 20)

        self.idLine = QComboBox(self)
        for item in self.user_service.get():
            self.idLine.addItem(item['id'])

        self.idLine.move(80, 20)
        self.idLine.resize(200, 32)

        self.combo_box_label = QLabel(self)
        self.combo_box_label.setText("Статус")
        self.combo_box_label.move(20, 70)

        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Работает")
        self.combo_box.addItem("Уволен")
        self.combo_box.move(80, 70)
        self.combo_box.resize(200, 32)

        button = QPushButton('Обновить', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 120)

    def __repr__(self):
        return "".format()

    def __del__(self):
        pass

    def clickMetod(self):
        user = self.user_service.get_by_id(self.idLine.currentText())
        status = self.combo_box.currentText()
        data = {
            'name': user['name'],
            'role': user['role'],
            'status': status,
        }
        self.user_service.update(data, user['id'])
        self.idLine.clear()
        self.close()

        a = ErrorException(title='Успех', text='Статус обновлен')
        self.window.append(a)
        a.show()


class OrderWindow(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.status_service = StatusService()
        self.user_service = UserService()
        self.role_service = RoleService()

        data_rows = []
        users = self.user_service.get()
        for user in users:
            data_rows.append(
                [user['id'], user['name'], self.role_service.get_by_id(user['role'])['name'], user['status']])

        self.size = QSize(600, 750)
        self.setFixedSize(self.size)
        self.setWindowTitle('AdminWindow')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_update_table = QAction(QIcon('img/ui/refresh.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        central = QWidget(self)
        self.setCentralWidget(central)
        self.grid = QGridLayout(self)
        central.setLayout(self.grid)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(self.order_service.count_orders())
        self.table.setHorizontalHeaderLabels(['ID', 'Статус', 'Начало', 'Окончание'])
        for i, v in enumerate(self.order_service.get()):
            self.table.setItem(i, 0, QTableWidgetItem(str(v['id'])))
            self.table.setItem(i, 1, QTableWidgetItem(str(self.status_service.get_by_id(v['status_id'])['name'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v['start_order'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v['end_order'])))

        self.grid.addWidget(self.table, 0, 0)

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = OrderWindow()
            self.window.append(a)
            a.show()


class FormCreateUser(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.user_service = UserService()
        self.role_service = RoleService()
        self.status_service = StatusService()

        self.setMinimumSize(QSize(320, 270))
        self.setWindowTitle('Создание пользователя')

        self.combo_box_label = QLabel(self)
        self.combo_box_label.setText("Роль")
        self.combo_box_label.move(20, 20)

        self.combo_box = QComboBox(self)
        for role in self.role_service.get():
            self.combo_box.addItem(str(role['name']))
        self.combo_box.move(110, 20)
        self.combo_box.resize(200, 32)

        self.combo_box_label_start = QLabel(self)
        self.combo_box_label_start.setText("Пароль")
        self.combo_box_label_start.move(20, 60)

        self.line_password = QLineEdit(self)
        self.line_password.move(110, 60)
        self.line_password.resize(200, 32)

        self.combo_box_end = QComboBox(self)
        self.combo_box_end.addItem('Работает')
        self.combo_box_end.addItem('Уволен')
        self.combo_box_end.move(110, 125)
        self.combo_box_end.resize(200, 32)

        self.combo_box_label_end = QLabel(self)
        self.combo_box_label_end.setText("Статус")
        self.combo_box_label_end.move(20, 125)

        self.line_name = QLineEdit(self)
        self.line_name.move(110, 160)
        self.line_name.resize(200, 32)

        self.line_name_label = QLabel(self)
        self.line_name_label.setText("Имя")
        self.line_name_label.move(20, 160)

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 225)

    def __repr__(self):
        return "".format()

    def __del__(self):
        pass

    def clickMetod(self):
        status = self.combo_box_end.currentText()
        role = self.role_service.get_by_name(self.combo_box.currentText())
        password = self.line_password.text()
        name = self.line_name.text()
        print(status, role, password, name)
        data = {
            "name": name,
            "role": role['id'],
            "password": password,
            "status": status,
        }
        self.user_service.create(data)
        self.close()

        a = ErrorException(title='Успех', text='Пользователь создан')
        self.window.append(a)
        a.show()


class Shifts(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.status_service = StatusService()
        self.user_service = UserService()
        self.role_service = RoleService()
        self.shift_service = ShiftService()
        self.shift_user_service = ShiftUserService()

        data_rows = []
        users = self.user_service.get()
        for user in users:
            data_rows.append(
                [user['id'], user['name'], self.role_service.get_by_id(user['role'])['name'], user['status']])

        self.size = QSize(600, 750)
        self.setFixedSize(self.size)
        self.setWindowTitle('AdminWindow')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_update_table = QAction(QIcon('img/ui/plus.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.call_create_shift)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/refresh.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        central = QWidget(self)
        self.setCentralWidget(central)
        self.grid = QGridLayout(self)
        central.setLayout(self.grid)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(*self.shift_user_service.count())
        self.table.setHorizontalHeaderLabels(['ID', 'Дата', 'Начало', 'Окончание', 'Пользователь'])
        for i, v in enumerate(self.shift_service.get()):
            self.table.setItem(i, 0, QTableWidgetItem(str(v[0])))
            self.table.setItem(i, 1, QTableWidgetItem(str(v[1])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v[2])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v[3])))
            id_users = [str(i['id_user']) for i in
                        self.shift_user_service.get_by_id(id=v[0])]
            self.table.setItem(i, 4, QTableWidgetItem(', '.join(id_users)))
        self.grid.addWidget(self.table, 0, 0)

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = Shifts()
            self.window.append(a)
            a.show()

    def call_create_shift(self, state):
        if state:
            self.close()
            a = FormCreateOrderWaiter()
            self.window.append(a)
            a.show()


class FormCreateOrderWaiter(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.status_service = StatusService()
        self.user_service = UserService()
        self.role_service = RoleService()
        self.shift_service = ShiftService()
        self.shift_user_service = ShiftUserService()

        self.setMinimumSize(QSize(320, 270))
        self.setWindowTitle('Создание смены')

        self.combo_box_label = QLabel(self)
        self.combo_box_label.setText("Дата")
        self.combo_box_label.move(20, 20)

        self.combo_box = QComboBox(self)
        for time in range(30):
            self.combo_box.addItem(str(time))
        self.combo_box.move(110, 20)
        self.combo_box.resize(200, 32)

        self.combo_box_label_start = QLabel(self)
        self.combo_box_label_start.setText("Начало работы")
        self.combo_box_label_start.move(20, 60)

        self.combo_box_start = QComboBox(self)
        for hour in range(24):
            for minute in range(0, 60, 15):
                time_value = hour + minute / 60
                time_str = f"{hour:02d}:{minute:02d}"
                self.combo_box_start.addItem(time_str)
        self.combo_box_start.move(110, 60)
        self.combo_box_start.resize(200, 32)

        self.combo_box_end = QComboBox(self)
        for hour in range(24):
            for minute in range(0, 60, 15):
                time_value = hour + minute / 60
                time_str = f"{hour:02d}:{minute:02d}"
                self.combo_box_end.addItem(time_str)
        self.combo_box_end.move(110, 125)
        self.combo_box_end.resize(200, 32)

        self.combo_box_label_end = QLabel(self)
        self.combo_box_label_end.setText("Конец работы")
        self.combo_box_label_end.move(20, 125)

        self.combo_box_label_user = QLabel(self)
        self.combo_box_label_user.setText("Пользователь")
        self.combo_box_label_user.move(20, 160)

        self.combo_user = QComboBox(self)
        for user in self.user_service.get():
            self.combo_user.addItem(str(user['id']))
        self.combo_user.move(110, 160)
        self.combo_user.resize(200, 32)

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 225)

    def __repr__(self):
        return "".format()

    def __del__(self):
        pass

    def clickMetod(self):
        user_id = self.combo_user.currentText()
        date = self.combo_box.currentText()
        start = self.combo_box_start.currentText()
        end = self.combo_box_end.currentText()
        self.shift_service.create(date, start, end)
        print(self.shift_service.get_by(date, start, end)['id'])
        self.shift_user_service.create(self.shift_service.get_by(date, start, end)['id'], user_id)
        self.close()

        a = ErrorException(title='Успех', text='Создано')
        self.window.append(a)
        a.show()
