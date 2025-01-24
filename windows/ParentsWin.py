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
        self.setGeometry(1130, 100, 770, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.update_btn = QPushButton('Изменить')
        self.delete_btn = QPushButton('Удалить')
        self.add_btn = QPushButton('Добавить')

        init_db()
        db = SessionLocal()

        self.parent_service = ParentService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id_parent', 'name', 'surname', 'phone_number', 'adress', 'passport_id',
                                              'parent_status'])
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

    def show_booksupdate_win(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            selected_book = {
                'id': self.model.item(row, 0).text(),
                'author': self.model.item(row, 1).text(),
                'book_name': self.model.item(row, 2).text(),
                'book_picture': self.model.item(row, 3).text(),
                'price': self.model.item(row, 4).text(),
            }
            self.booksaddorupdate_win = BooksAddOrUpdateWin(self, selected_book)
            self.booksaddorupdate_win.show()
        else:
            QMessageBox.information(self, 'Информация', 'Для выбора записи, нажмите на её номер в таблице',
            QMessageBox.StandardButton.Ok)


    def show_booksadd_win(self):
        self.booksaddorupdate_win = BooksAddOrUpdateWin(self)

        self.booksaddorupdate_win.show()

    def delete_book(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            dialog = QMessageBox()
            dialog.setGeometry(1200, 275, 400, 400)
            dialog.setWindowTitle("Подтверждение")
            dialog.setText(f"Вы уверены, что хотите удалить запись?")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            user_response = dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                self.books_service.delete_book(self.model.item(row, 0).text())
                QMessageBox.information(self, "Инфо", 'Запись удалена')
                self.model.clear()
                self.model.setHorizontalHeaderLabels(['id', 'Автор', 'Название', 'Картинка', 'Цена'])
                self.load_books()
        else:
            QMessageBox.information(self, 'Информация', 'Для удаления записи, нажмите на её номер в таблице',
            QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        try:
            if self.booksaddorupdate_win.isVisible():
                self.booksaddorupdate_win.close()
        except AttributeError:
            pass
        finally:
            event.accept()
