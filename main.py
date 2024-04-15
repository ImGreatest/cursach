import sys
from PySide6.QtWidgets import QApplication
from pages.admin_window import AdminWindow
from pages.auth import Auth


def main():
    window = []
    app = QApplication(sys.argv)
    auth_window = Auth()
    # admin = AdminWindow()
    # window.append(admin)
    window.append(auth_window)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
