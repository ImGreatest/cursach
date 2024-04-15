from PySide6.QtCore import QSize
from PySide6.QtWidgets import QPushButton, QLabel, QMainWindow


class ErrorException(QMainWindow):
    def __init__(self, title: str, text: str):
        QMainWindow.__init__(self)

        self._title = title
        self._text = text
        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle('{}'.format(self._title))

        label = QLabel(self)
        label.setText('{}'.format(self._text))
        label.move(20, 20)
        label.resize(300, 20)

        button = QPushButton('Ok', self)
        button.clicked.connect(self.clickMetod)
        button.resize(200, 32)
        button.move(80, 90)

    def __repr__(self):
        return "".format()

    def clickMetod(self):
        self.close()
