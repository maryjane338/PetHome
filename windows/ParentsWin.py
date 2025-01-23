from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *
from database import SessionLocal, init_db
from services.service import ParentService


class ParentsWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Книги')
        self.setGeometry(1150, 100, 400, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.update_btn = QPushButton('Изменить')
        self.update_btn.clicked.connect(self.show_booksupdate_win)
        self.delete_btn = QPushButton('Удалить')
        self.delete_btn.clicked.connect(self.delete_book)
        self.add_btn = QPushButton('Добавить')
        self.add_btn.clicked.connect(self.show_booksadd_win)

        init_db()
        db = SessionLocal()

        self.parent_service = ParentService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id', 'Автор', 'Название', 'Картинка', 'Цена', 'Цеkjна', 'gfgfh'])
        self.view.setModel(self.model)

        self.load_books()

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.update_btn)
        v_l.addWidget(self.delete_btn)
        v_l.addWidget(self.add_btn)
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def load_books(self):
        orders = self.parent_service.get_all_parents()
        for order in orders:
            row = [QStandardItem(field) for field in order]
            self.model.appendRow(row)

    def closeEvent(self, event):
        try:
            if self.booksaddorupdate_win.isVisible():
                self.booksaddorupdate_win.close()
        except AttributeError:
            pass
        finally:
            event.accept()
