from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from database import SessionLocal
from services.service import PetService, ShelterService


# from services.book_service import BookService


class ShelterAddOrUpdateWin(QWidget):
    def __init__(self, shelter_win, shelter=None):
        super().__init__()
        self.shelter_win = shelter_win
        self.shelter = shelter
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ')
        self.setGeometry(1550, 600, 150, 150)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        id_parent_label = QLabel('Введите ID родителя:')
        self.id_parent_input = QLineEdit()
        id_pet_label = QLabel('Введите ID питомца:')
        self.id_pet_input = QLineEdit()
        self.save_btn = QPushButton('Сохранить')
        self.save_btn.clicked.connect(self.save_shelter)
        self.id = QLineEdit()

        if self.shelter:
            self.id_parent_input.setText(self.shelter['parent_name'])
            self.id_pet_input.setText(self.shelter['pet_name'])
            self.id.setText(self.shelter['id_shelter'])

        main_l = QVBoxLayout()
        main_l.addWidget(id_parent_label)
        main_l.addWidget(self.id_parent_input)
        main_l.addWidget(id_pet_label)
        main_l.addWidget(self.id_pet_input)
        main_l.addStretch()
        main_l.addWidget(self.save_btn)
        self.setLayout(main_l)

    def save_shelter(self):
        db = SessionLocal()
        shelter_service = ShelterService(db)

        try:
            int(self.id_parent_input.text())
            int(self.id_pet_input.text())

            if self.id_pet_input.text() == '' or self.id_parent_input.text() == '':
                QMessageBox.information(self, 'Информация',
                                        'Вы не заполнили все поля или заполнили их некорректно.')
            else:
                check_guys = shelter_service.check_parent_and_pet(
                    parent_name=self.id_parent_input.text(),
                    pet_name=self.id_pet_input.text(),
                )
                if check_guys == 1:
                    QMessageBox.information(self, 'Информация', 'Такого питомца или родителя не существует')
                elif self.id.text():
                    shelter_service.update_shelter(
                        id_shelter=self.id.text(),
                        parent_name=self.id_parent_input.text(),
                        pet_name=self.id_pet_input.text(),
                    )
                else:
                    answer = shelter_service.check_status(self.id_pet_input.text())
                    print(answer)
                    if answer == 1:
                        QMessageBox.information(self, 'Информация', 'Этот питомец уже усыновлён')
                    else:
                        shelter_service.add_shelter(
                            parent_name=int(self.id_parent_input.text()),
                            pet_name=int(self.id_pet_input.text()),
                        )
                QMessageBox.information(self, 'Информация', 'Книга успешно сохранена!')
                self.close()
                self.shelter_win.model.clear()
                self.shelter_win.model.setHorizontalHeaderLabels(['id_shelter', 'parent_name', 'pet_name'])
                self.shelter_win.load_users()

        except ValueError:
            QMessageBox.information(self, 'Информация',
                                    'Вы не заполнили все поля или заполнили их некорректно.')
