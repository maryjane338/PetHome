from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from database import SessionLocal, init_db
from services.service import EventService
from windows.events_windows.EventAddOrUpdateWin import EventAddOrUpdateWin


class EventsWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Мероприятия')
        self.setGeometry(0, 600, 350, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('pictures/dog.png'))

        self.add_btn = QPushButton('Добавить')
        self.add_btn.clicked.connect(self.show_event_add_win)
        self.update_btn = QPushButton('Изменить')
        self.update_btn.clicked.connect(self.show_event_update_win)
        self.delete_btn = QPushButton('Удалить')
        self.delete_btn.clicked.connect(self.delete_event)

        init_db()
        db = SessionLocal()

        self.event_service = EventService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id_event', 'event_name', 'event_date'])
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
        events = self.event_service.get_all_events()
        for event in events:
            row = [QStandardItem(field) for field in event]
            self.model.appendRow(row)

    def show_event_update_win(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            selected_event = {
                'id': self.model.item(row, 0).text(),
                'name': self.model.item(row, 1).text(),
                'date': self.model.item(row, 2).text()
            }
            self.event_add_or_update_win = EventAddOrUpdateWin(self, selected_event)
            self.event_add_or_update_win.show()
        else:
            QMessageBox.information(self, 'Информация', 'Для выбора записи, нажмите на её номер в таблице',
            QMessageBox.StandardButton.Ok)

    def show_event_add_win(self):
        self.event_add_or_update_win = EventAddOrUpdateWin(self)
        self.event_add_or_update_win.show()

    def delete_event(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            dialog = QMessageBox()
            dialog.setGeometry(50, 650, 350, 400)
            dialog.setWindowTitle("Подтверждение")
            dialog.setText(f"Вы уверены, что хотите удалить запись?")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            user_response = dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                self.event_service.delete_event(self.model.item(row, 0).text())
                QMessageBox.information(self, "Инфо", 'Запись удалена')
                self.model.clear()
                self.model.setHorizontalHeaderLabels(['id_event', 'event_name', 'event_date'])
                self.load_users()
        else:
            QMessageBox.information(self, 'Информация', 'Для удаления записи, нажмите на её номер в таблице',
            QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        try:
            if self.event_add_or_update_win.isVisible():
                self.event_add_or_update_win.close()
        except AttributeError:
            pass
        finally:
            event.accept()
