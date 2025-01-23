from PyQt6.QtWidgets import *
from database import init_db, SessionLocal
# from services.book_service import AdminService
from windows.mainWindow import MainWin


class AuthorizationWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 200)
        self.setWindowTitle('Приют для животных')
        self.setFixedSize(self.width(), self.height())

        login = QLabel('Введите логин:(Вова)')
        self.login_line = QLineEdit()
        password = QLabel('Введите пароль:(123)')
        self.password_line = QLineEdit()
        self.enter_btn = QPushButton('Войти')
        self.enter_btn.clicked.connect(self.enter)

        main_l = QVBoxLayout()
        main_l.addWidget(login)
        main_l.addWidget(self.login_line)
        main_l.addWidget(password)
        main_l.addWidget(self.password_line)
        main_l.addWidget(self.enter_btn)
        main_l.addStretch()
        self.setLayout(main_l)

    def enter(self):
        if self.password_line.text() == self.password_line.text():
            self.main_win = MainWin(self)
            self.main_win.show()
            self.close()
        else:
            QMessageBox.information(self, 'Инфо', 'Администратора с таким логином или паролем не существует!\n'
                                                  'Попробуйте ещё раз.')

    def back(self):
        self.close()
        self.enter_win.show()
