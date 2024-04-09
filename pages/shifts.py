from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow

from data.order import OrderService


class ShiftPanel(QMainWindow):
    def __init__(self):
        self.window = []
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(940, 800))
        self.setWindowTitle('Login window')

        self.order_service = OrderService()

    def __repr__(self):
        pass

    def __del__(self):
        pass
