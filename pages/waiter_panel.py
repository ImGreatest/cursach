from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QMenuBar, QToolBar, QStatusBar, QTableWidgetItem, QTableWidget, QGridLayout, \
    QWidget

from data.order import OrderService


class WaiterPanel(QMainWindow):
    def __init__(self):

        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()

        self.setMinimumSize(QSize(940, 800))
        self.setWindowTitle('Login window')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_set_status = QAction(QIcon('img/ui/arrow-circle-double-135.png'), 'Обновить статус', self)
        toolbar_button_set_status.setStatusTip('Обновить статус')
        toolbar_button_set_status.setCheckable(True)
        toolbar_button_set_status.triggered.connect(self.callForm)
        toolbar.addAction(toolbar_button_set_status)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_update_table = QAction(QIcon('img/ui/arrow-circle-double-135.png'), 'Обновить таблицу', self)
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
            self.table.setItem(i, 1, QTableWidgetItem(str(v['status_id'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v['start_order'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v['end_order'])))

        self.grid.addWidget(self.table, 0, 0)

    def __repr__(self):
        return "".format()

    def __del__(self):
        pass
