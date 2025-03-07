from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import *
from database import init_db, SessionLocal
from services.service import WorkerService
# from services.book_service import AdminService
from windows.mainWindow import MainWin


class AuthorizationWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(415, 350)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('Учёт питомцев')
        self.setWindowIcon(QIcon('pictures/dog.png'))

        self.pixmap = QPixmap()
        self.pixmap.load('pictures/uchet_pitomcev.png')
        scaled_pixmap = self.pixmap.scaled(400, 130)
        self.label = QLabel()
        self.label.setPixmap(scaled_pixmap)

        login = QLabel('Введите логин:')
        self.login_line = QLineEdit()
        self.login_line.setPlaceholderText('Вова')
        password = QLabel('Введите пароль:')
        self.password_line = QLineEdit()
        self.password_line.setPlaceholderText('123')
        self.enter_btn = QPushButton('Войти')
        self.enter_btn.clicked.connect(self.enter)

        main_l = QVBoxLayout()
        main_l.addWidget(self.label)
        main_l.addWidget(login)
        main_l.addWidget(self.login_line)
        main_l.addWidget(password)
        main_l.addWidget(self.password_line)
        main_l.addStretch()
        main_l.addWidget(self.enter_btn)
        self.setLayout(main_l)

    def enter(self):
        init_db()
        db = SessionLocal()

        worker_service = WorkerService(db)
        worker_password = worker_service.select_worker_for_enter(self.login_line.text())
        if self.password_line.text() == worker_password:
            self.main_win = MainWin(self)
            self.main_win.show()
            self.close()
        else:
            QMessageBox.information(self, 'Инфо', 'Администратора с таким логином или паролем не существует!\n'
                                                  'Попробуйте ещё раз.')

    def back(self):
        self.close()
        self.enter_win.show()
