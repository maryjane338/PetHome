from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *
from database import SessionLocal, init_db
from services.service import PetService


# from services.book_service import OrderService
# from windows.admin.UpdateOrderWin import UpdateOrderWin


class UnhomePetsWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказы')
        self.setGeometry(50, 300, 750, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.update_btn = QPushButton('Изменить')
        self.update_btn.clicked.connect(self.show_update_win)
        self.delete_btn = QPushButton('Удалить')
        self.delete_btn.clicked.connect(self.delete_order)

        init_db()
        db = SessionLocal()

        self.pet_service = PetService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id_order', 'user_name', 'Книга', 'Адрес доставки', 'Способ оплаты',
                                              'Дата доставки'])
        self.view.setModel(self.model)

        self.load_orders()

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.update_btn)
        v_l.addWidget(self.delete_btn)
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def load_orders(self):
        orders = self.pet_service.get_all_pet()
        for order in orders:
            row = [QStandardItem(field) for field in order]
            self.model.appendRow(row)

    def show_update_win(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            selected_order = {  # Собираем данные выбранной строки
                'id_order': self.model.item(row, 0).text(),
                'user_name': self.model.item(row, 1).text(),
                'book_name': self.model.item(row, 2).text(),
                'address': self.model.item(row, 3).text(),
                'payment': self.model.item(row, 4).text(),
                'delivery_date': self.model.item(row, 5).text(),
            }
            self.update_order_win = UpdateOrderWin(self, selected_order)
            self.update_order_win.show()
        else:
            QMessageBox.information(self, 'Информация', 'Для выбора записи, нажмите на её номер в таблице',
                                    QMessageBox.StandardButton.Ok)

    def delete_order(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            dialog = QMessageBox()
            dialog.setGeometry(275, 450, 750, 400)
            dialog.setWindowTitle("Подтверждение")
            dialog.setText(f"Вы уверены, что хотите удалить заказ?")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            user_response = dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                self.order_service.delete_order(self.model.item(row, 0).text())
                QMessageBox.information(self, "Инфо", 'Заказ удалена')
                self.model.clear()
                self.model.setHorizontalHeaderLabels(
                    ['id_order', 'user_name', 'Книга', 'Адрес доставки', 'Способ оплаты',
                     'Дата доставки'])
                self.load_orders()
        else:
            QMessageBox.information(self, 'Информация', 'Для удаления заказа, нажмите на его номер в таблице',
                                    QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        try:
            if self.update_order_win.isVisible():
                self.update_order_win.close()
        except AttributeError:
            pass
        finally:
            event.accept()

