from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *

from windows.EventsWin import EventsWin
from windows.ParentsWin import ParentsWin
from windows.ShelterWin import SheltersWin
from windows.UnhomePetsWin import UnhomePetsWin


class MainWin(QWidget):
    def __init__(self, enter_win):
        super().__init__()
        self.enter_win = enter_win
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Окно Сотрудника')
        self.resize(300, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.all_pets_btn = QPushButton('Животные в приюте')
        self.all_pets_btn.clicked.connect(self.show_all_orders_win)

        self.all_parents_btn = QPushButton('Родители')
        self.all_parents_btn.clicked.connect(self.show_books_win)

        self.home_pets_btn = QPushButton('Домашние животные')
        self.home_pets_btn.clicked.connect(self.show_users_win)

        self.events_btn = QPushButton('Мероприятия')
        self.events_btn.clicked.connect(self.show_events_win)

        self.back_enter_btn = QPushButton('Вернуться ко входу')
        self.back_enter_btn.clicked.connect(self.back_to_enter)

        self.main_l = QVBoxLayout()
        self.main_l.addStretch()
        self.main_l.addWidget(self.all_pets_btn)
        self.main_l.addWidget(self.all_parents_btn)
        self.main_l.addWidget(self.home_pets_btn)
        self.main_l.addWidget(self.events_btn)
        self.main_l.addStretch()
        self.main_l.addWidget(self.back_enter_btn)
        self.setLayout(self.main_l)

        self.win1 = 0
        self.win2 = 0
        self.win3 = 0

    def show_books_win(self):
        self.books_win = ParentsWin()
        self.books_win.show()
        self.win1 = 1

    def show_all_orders_win(self):
        self.adm_orders_win = UnhomePetsWin()
        self.adm_orders_win.show()
        self.win2 = 1

    def show_users_win(self):
        self.users_win = SheltersWin()
        self.users_win.show()
        self.win3 = 1

    def show_events_win(self):
        self.events_win = EventsWin()
        self.events_win.show()
        self.win4 = 1

    def back_to_enter(self):
        if self.win1 == 1 and self.win2 == 1 and self.win3 == 1:
            self.books_win.close()
            self.adm_orders_win.close()
            self.users_win.close()
            self.hide()
        elif self.win1 == 0 and self.win2 == 0 and self.win3 == 0:
            self.hide()
        elif self.win1 == 1 and self.win2 == 1:
            self.books_win.close()
            self.adm_orders_win.close()
            self.hide()
        elif self.win2 == 1 and self.win3 == 1:
            self.adm_orders_win.close()
            self.users_win.close()
            self.hide()
        elif self.win3 == 1 and self.win1 == 1:
            self.users_win.close()
            self.books_win.close()
            self.hide()
        elif self.win1 == 1:
            self.books_win.close()
            self.hide()
        elif self.win2 == 1:
            self.adm_orders_win.close()
            self.hide()
        elif self.win3 == 1:
            self.users_win.close()
            self.hide()
        self.enter_win.show()

    def closeEvent(self, event):
        QApplication.quit()
