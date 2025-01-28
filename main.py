from PyQt6.QtWidgets import QApplication
from windows.enterWin import EnterWin
import sys


def main():
    app = QApplication([])
    win = EnterWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
