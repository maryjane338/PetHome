from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *
from database import SessionLocal, init_db
from services.service import PetService
from windows.pets_windows.PetsAddOrUpdateWin import PetsAddOrUpdateWin


class UnhomePetsWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Животные')
        self.setGeometry(0, 35, 630, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('pictures/dog.png'))

        self.update_btn = QPushButton('Изменить')
        self.update_btn.clicked.connect(self.show_update_win)
        self.add_btn = QPushButton('Добавить')
        self.add_btn.clicked.connect(self.show_add_win)
        self.delete_btn = QPushButton('Удалить')
        self.delete_btn.clicked.connect(self.delete_order)

        init_db()
        db = SessionLocal()

        self.pet_service = PetService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id_pet', 'pet_name', 'animal_species', 'age', 'weight', 'home_status'])
        self.view.setModel(self.model)

        self.load_orders()

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.update_btn)
        v_l.addWidget(self.add_btn)
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
            selected_pet = {
                'id_pet': self.model.item(row, 0).text(),
                'pet_name': self.model.item(row, 1).text(),
                'animal_species': self.model.item(row, 2).text(),
                'age': self.model.item(row, 3).text(),
                'weight': self.model.item(row, 4).text(),
                'home_status': self.model.item(row, 5).text(),
            }
            self.pets_add_or_update_win = PetsAddOrUpdateWin(self, selected_pet)
            self.pets_add_or_update_win.show()
        else:
            QMessageBox.information(self, 'Информация', 'Для выбора записи, нажмите на её номер в таблице',
                                    QMessageBox.StandardButton.Ok)

    def show_add_win(self):
        self.pets_add_or_update_win = PetsAddOrUpdateWin(self)
        self.pets_add_or_update_win.show()

    def delete_order(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            dialog = QMessageBox()
            dialog.setGeometry(275, 450, 750, 400)
            dialog.setWindowTitle("Подтверждение")
            dialog.setText(f"Вы уверены, что хотите удалить запись?")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            user_response = dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                self.pet_service.delete_pet(self.model.item(row, 0).text())
                QMessageBox.information(self, "Инфо", 'Запись удалена')
                self.model.clear()
                self.model.setHorizontalHeaderLabels(
                    ['id_pet', 'pet_name', 'animal_species', 'age', 'weight', 'home_status'])
                self.load_orders()
        else:
            QMessageBox.information(self, 'Информация', 'Для удаления записи, нажмите на её номер в таблице',
                                    QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        try:
            if self.pets_add_or_update_win.isVisible():
                self.pets_add_or_update_win.close()
        except AttributeError:
            pass
        finally:
            event.accept()