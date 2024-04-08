from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from data.role import RoleService
from data.user import UserService


class AdminWindow(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.user_service = UserService()
        self.role_service = RoleService()

        data_rows = []
        users = self.user_service.get()
        for user in users:
            data_rows.append(
                [user['id'], user['name'], self.role_service.get_by_id(user['role'])['name'], user['status']])

        self.size = QSize(940, 800)
        self.setFixedSize(self.size)
        self.setWindowTitle('AdminWindow')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_create = QAction(QIcon('img/ui/new.png'), 'Смены', self)
        toolbar_button_create.setStatusTip('Смены')
        toolbar_button_create.setCheckable(True)
        # toolbar_button_create.triggered.connect(self.callFormCreateGood)
        toolbar.addAction(toolbar_button_create)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_delete = QAction(QIcon('img/ui/minus.png'), 'Уволить', self)
        toolbar_button_delete.setStatusTip('Уволить')
        toolbar_button_delete.setCheckable(True)
        # toolbar_button_delete.triggered.connect(self.callFormDeleteGood)
        toolbar.addAction(toolbar_button_delete)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_delete_user = QAction(QIcon('img/ui/bauble.png'), 'Создать пользователя', self)
        toolbar_button_delete_user.setStatusTip('Создать пользователя')
        toolbar_button_delete_user.setCheckable(True)
        # toolbar_button_delete_user.triggered.connect(self.callFormDeleteUser)
        toolbar.addAction(toolbar_button_delete_user)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/arrow-circle-double-135.png'), 'Обновить таблицу', self)
        toolbar_button_update_table.setStatusTip('Обновить таблицу')
        toolbar_button_update_table.setCheckable(True)
        toolbar_button_update_table.triggered.connect(self.callUpdateTable)
        toolbar.addAction(toolbar_button_update_table)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        self.show()

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = AdminWindow()
            self.window.append(a)
            a.show()
