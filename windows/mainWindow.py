from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from windows.events_windows.EventsWin import EventsWin
from windows.parents_windows.ParentsWin import ParentsWin
from windows.pets_windows.PetsWin import PetsWin
from windows.shelters_windows.ShelterWin import SheltersWin


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

        self.books_win = None
        self.adm_orders_win = None
        self.users_win = None
        self.events_win = None

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
        if self.books_win is not None:
            self.books_win.close()
            self.books_win = None

        if self.adm_orders_win is not None:
            self.adm_orders_win.close()
            self.adm_orders_win = None

        if self.users_win is not None:
            self.users_win.close()
            self.users_win = None

        if self.events_win is not None:
            self.events_win.close()
            self.events_win = None

        self.hide()
        self.enter_win.show()

    def closeEvent(self, event):
        QApplication.quit()
