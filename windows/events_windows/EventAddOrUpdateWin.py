from datetime import date
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from database import SessionLocal
from services.service import EventService


class EventAddOrUpdateWin(QWidget):
    def __init__(self, events_win, event=None):
        super().__init__()
        self.events_win = events_win
        self.event = event
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Мероприятия')
        self.setGeometry(350, 600, 300, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('pictures/dog.png'))

        name_label = QLabel('Введите название события:')
        self.name_input = QLineEdit()
        date_label = QLabel('Введите дату мероприятия (гг.мм.дд.):')
        self.date_input = QLineEdit()
        self.save_btn = QPushButton('Сохранить')
        self.id = QLineEdit()
        self.save_btn.clicked.connect(self.save_event)

        if self.event:
            self.name_input.setText(self.event['name'])
            self.date_input.setText(self.event['date'])
            self.id.setText(self.event['id'])

        main_l = QVBoxLayout()
        main_l.addWidget(name_label)
        main_l.addWidget(self.name_input)
        main_l.addWidget(date_label)
        main_l.addWidget(self.date_input)
        main_l.addStretch()
        main_l.addWidget(self.save_btn)
        self.setLayout(main_l)

    def save_event(self):
        db = SessionLocal()
        event_service = EventService(db)

        try:
            date_text = self.date_input.text()
            date_text_check = list(date_text)
            if len(date_text_check) != 8:
                QMessageBox.information(self, 'Информация',
                                        'Вы не заполнили все поля или заполнили их некорректно.')
            elif date_text_check[4] != '-' and date_text_check[7] != '-':
                QMessageBox.information(self, 'Информация',
                                        'Вы не заполнили все поля или заполнили их некорректно.')
            else:
                date_list = list(date_text.split('-'))
                int(date_list[0])
                int(date_list[1])
                int(date_list[2])

                if self.name_input.text() == '' or self.date_input.text() == '' or len(date_list[0]) != 4\
                        or len(date_list[1]) != 2 or len(date_list[2]) != 2 and len(date_text_check) != 8:
                    QMessageBox.information(self, 'Информация',
                                            'Вы не заполнили все поля или заполнили их некорректно.')
                else:
                    if self.id.text():
                        event_service.update_event(
                            id_event=self.id.text(),
                            event_name=self.name_input.text(),
                            event_date=date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
                        )
                    else:
                        event_service.add_event(
                            event_name=self.name_input.text(),
                            event_date=date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
                        )
                    QMessageBox.information(self, 'Информация', 'Запись успешно сохранена!')
                    self.close()
                    self.events_win.model.clear()
                    self.events_win.model.setHorizontalHeaderLabels(['id_event', 'event_name', 'event_date'])
                    self.events_win.load_users()

        except ValueError:
            QMessageBox.information(self, 'Информация',
                                    'Вы не заполнили все поля или заполнили их некорректно.')
