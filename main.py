from PyQt6.QtWidgets import QApplication
from windows.enterWin import AuthorizationWin
import sys


def main():
    app = QApplication([])
    win = AuthorizationWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
