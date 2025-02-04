from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from database import SessionLocal
from services.service import ParentService


# from services.book_service import BookService


class ParentAddOrUpdateWin(QWidget):
    def __init__(self, bookswin, book=None):
        super().__init__()
        self.bookswin = bookswin
        self.book = book
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ')
        self.setGeometry(1550, 100, 300, 300)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        name_label = QLabel('Введите имя:')
        self.name_input = QLineEdit()
        surname_label = QLabel('Введите фамилию:')
        self.surname_input = QLineEdit()
        phone_num_label = QLabel('Введите номер телефона:')
        self.phone_num_input = QLineEdit()
        address_label = QLabel('Введите адрес:')
        self.address_input = QLineEdit()
        passport_label = QLabel('Введите серию паспорта:')
        self.passport_input = QLineEdit()
        self.save_btn = QPushButton('Сохранить')
        self.id = QLineEdit()
        self.save_btn.clicked.connect(self.save_book)

        if self.book:
            self.name_input.setText(self.book['name'])
            self.surname_input.setText(self.book['surname'])
            self.phone_num_input.setText(self.book['phone_number'])
            self.address_input.setText(self.book['address'])
            self.passport_input.setText(self.book['passport_id'])
            self.id.setText(self.book['id'])

        main_l = QVBoxLayout()
        main_l.addWidget(name_label)
        main_l.addWidget(self.name_input)
        main_l.addWidget(surname_label)
        main_l.addWidget(self.surname_input)
        main_l.addWidget(phone_num_label)
        main_l.addWidget(self.phone_num_input)
        main_l.addWidget(address_label)
        main_l.addWidget(self.address_input)
        main_l.addWidget(passport_label)
        main_l.addWidget(self.passport_input)
        main_l.addStretch()
        main_l.addWidget(self.save_btn)
        self.setLayout(main_l)

    def save_book(self):
        db = SessionLocal()
        book_service = ParentService(db)

        try:
            int(self.phone_num_input.text())

            if self.name_input.text() == '' or self.surname_input.text() == '' or self.phone_num_input.text() == ''\
                    or self.address_input.text() == '' or self.passport_input.text() == '':
                QMessageBox.information(self, 'Информация',
                                        'Вы не заполнили все поля или заполнили их некорректно.')
            else:
                if self.id.text():
                    book_service.update_book(
                        id_book=self.id.text(),
                        author=self.name_input.text(),
                        book_name=self.surname_input.text(),
                        book_picture=self.phone_num_input.text(),
                        price=self.address_input.text()
                    )
                else:
                    book_service.add_book(
                        author=self.author_name_input.text(),
                        book_name=self.book_input.text(),
                        book_picture=f'book_pictures/{self.picture_input.text()}',
                        price=int(self.price_input.text())
                    )
                QMessageBox.information(self, 'Информация', 'Книга успешно сохранена!')
                self.close()
                self.bookswin.model.clear()
                self.bookswin.model.setHorizontalHeaderLabels(['id', 'Автор', 'Название', 'Картинка', 'Цена'])
                self.bookswin.load_books()

        except ValueError:
            QMessageBox.information(self, 'Информация',
                                    'Вы не заполнили все поля или заполнили их некорректно.')
