from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from database import SessionLocal, init_db
from services.service import EventService


class EventsWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Мероприятия')
        self.setGeometry(50, 600, 350, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

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
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def load_users(self):
        events = self.event_service.get_all_events()
        for event in events:
            row = [QStandardItem(field) for field in event]
            self.model.appendRow(row)
