from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QMenuBar, QToolBar, QStatusBar, QTableWidgetItem, QTableWidget, QGridLayout, \
    QWidget, QComboBox, QLabel, QPushButton

from data.order import OrderService
from data.status import StatusService
from pages.exceptions.error_dialog import ErrorException


class WaiterPanel(QMainWindow):
    def __init__(self):

        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.status_service = StatusService()

        self.setMinimumSize(QSize(940, 800))
        self.setWindowTitle('Login window')

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar_button_create_order = QAction(QIcon('img/ui/plus.png'), 'Создать заказ', self)
        toolbar_button_create_order.setStatusTip('Создать заказ')
        toolbar_button_create_order.setCheckable(True)
        toolbar_button_create_order.triggered.connect(self.callCreateForm)
        toolbar.addAction(toolbar_button_create_order)
        self.setStatusBar(QStatusBar(self))

        toolbar.addSeparator()

        toolbar_button_set_status = QAction(QIcon('img/ui/book-alt.png'), 'Обновить статус', self)
        toolbar_button_set_status.setStatusTip('Обновить статус')
        toolbar_button_set_status.setCheckable(True)
        toolbar_button_set_status.triggered.connect(self.callForm)
        toolbar.addAction(toolbar_button_set_status)
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
        self.table.setHorizontalHeaderLabels(['ID', 'Статус', 'Начало', 'Окончание'])
        for i, v in enumerate(self.order_service.get()):
            self.table.setItem(i, 0, QTableWidgetItem(str(v['id'])))
            self.table.setItem(i, 1, QTableWidgetItem(str(self.status_service.get_by_id(v['status_id'])['name'])))
            self.table.setItem(i, 2, QTableWidgetItem(str(v['start_order'])))
            self.table.setItem(i, 3, QTableWidgetItem(str(v['end_order'])))

        self.grid.addWidget(self.table, 0, 0)

    def __repr__(self):
        return "".format()

    def __del__(self):
        pass

    def callUpdateTable(self, state):
        if state:
            self.close()
            a = WaiterPanel()
            self.window.append(a)
            a.show()

    def callForm(self, state):
        if state:
            f = FormChangeStatusWaiter()
            self.window.append(f)
            f.show()

    def callCreateForm(self, state):
        if state:
            f = FormCreateOrderWaiter()
            self.window.append(f)
            f.show()


class FormCreateOrderWaiter(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.status_service = StatusService()

        self.setMinimumSize(QSize(320, 270))
        self.setWindowTitle('Создание заказа')

        self.combo_box_label = QLabel(self)
        self.combo_box_label.setText("Статус")
        self.combo_box_label.move(20, 20)

        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Принят")
        self.combo_box.addItem("Оплачен")
        self.combo_box.addItem("Готовится")
        self.combo_box.addItem("Готов")
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

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 225)

    def __repr__(self):
        return "".format()

    def __del__(self):
        pass

    def clickMetod(self):
        # id = self.idLine.currentText()
        status = self.status_service.get_by_name(self.combo_box.currentText())
        start = self.combo_box_start.currentText()
        end_work = self.combo_box_end.currentText()
        self.order_service.create(status['id'], start, end_work)
        self.close()

        a = ErrorException(title='Успех', text='Создано')
        self.window.append(a)
        a.show()


class FormChangeStatusWaiter(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.order_service = OrderService()
        self.status_service = StatusService()

        self.setMinimumSize(QSize(320, 180))
        self.setWindowTitle('Создание заказа')

        self.idLabel = QLabel(self)
        self.idLabel.setText('ID:')
        self.idLabel.move(20, 20)

        self.idLine = QComboBox(self)
        for item in self.order_service.get():
            self.idLine.addItem(item['id'])

        self.idLine.move(80, 20)
        self.idLine.resize(200, 32)

        self.combo_box_label = QLabel(self)
        self.combo_box_label.setText("Статус")
        self.combo_box_label.move(20, 70)

        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Принят")
        self.combo_box.addItem("Оплачен")
        self.combo_box.move(80, 70)
        self.combo_box.resize(200, 32)

        button = QPushButton('Создать', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 120)

    def __repr__(self):
        return "".format()

    def __del__(self):
        pass

    def clickMetod(self):
        id = self.idLine.currentText()
        status = self.status_service.get_by_name(self.combo_box.currentText())
        order = self.order_service.get_by_id(id)
        self.order_service.update(status['id'], order['start_order'], order['end_order'], id)
        self.idLine.clear()
        self.close()

        a = ErrorException(title='Успех', text='Статус обновлен')
        self.window.append(a)
        a.show()

