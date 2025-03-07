from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from database import SessionLocal, init_db
from services.service import ShelterService
from windows.shelters_windows.ShelterAddOrUpdateWin import ShelterAddOrUpdateWin


class SheltersWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Дом для животных')
        self.setGeometry(1570, 600, 340, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('pictures/dog.png'))

        self.update_btn = QPushButton('Изменить')
        self.update_btn.clicked.connect(self.show_update_win)
        self.add_btn = QPushButton('Добавить')
        self.add_btn.clicked.connect(self.show_add_win)
        self.delete_btn = QPushButton('Удалить')
        self.delete_btn.clicked.connect(self.delete_shelter)

        init_db()
        db = SessionLocal()

        self.shelter_service = ShelterService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id_shelter', 'parent_name', 'pet_name'])
        self.view.setModel(self.model)

        self.load_users()

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.add_btn)
        v_l.addWidget(self.update_btn)
        v_l.addWidget(self.delete_btn)
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def load_users(self):
        shelters = self.shelter_service.get_all_shelters()
        for shelter in shelters:
            row = [QStandardItem(field) for field in shelter]
            self.model.appendRow(row)

    def show_update_win(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            selected_shelter = {
                'id_shelter': self.model.item(row, 0).text(),
                'parent_name': self.model.item(row, 1).text(),
                'pet_name': self.model.item(row, 2).text(),
            }
            self.shelter_add_or_update_win = ShelterAddOrUpdateWin(self, selected_shelter)
            self.shelter_add_or_update_win.show()
        else:
            QMessageBox.information(self, 'Информация', 'Для выбора записи, нажмите на её номер в таблице',
                                    QMessageBox.StandardButton.Ok)

    def show_add_win(self):
        self.shelter_add_or_update_win = ShelterAddOrUpdateWin(self)
        self.shelter_add_or_update_win.show()

    def delete_shelter(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            dialog = QMessageBox()
            dialog.setGeometry(1200, 775, 400, 400)
            dialog.setWindowTitle("Подтверждение")
            dialog.setText(f"Вы уверены, что хотите удалить запись?")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            user_response = dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                self.shelter_service.delete_shelter(self.model.item(row, 0).text(), self.model.item(row, 2).text())
                QMessageBox.information(self, "Инфо", 'Запись удалена')
                self.model.clear()
                self.model.setHorizontalHeaderLabels(['id_shelter', 'parent_name', 'pet_name'])
                self.load_users()
        else:
            QMessageBox.information(self, 'Информация',
                                    'Для удаления записи, нажмите на её номер в таблице',
                                    QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        try:
            if self.shelter_add_or_update_win.isVisible():
                self.shelter_add_or_update_win.close()
        except AttributeError:
            pass
        finally:
            event.accept()
