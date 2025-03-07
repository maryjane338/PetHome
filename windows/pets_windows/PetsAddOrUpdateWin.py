from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from database import SessionLocal
from services.service import PetService


class PetsAddOrUpdateWin(QWidget):
    def __init__(self, pets_win, pet=None):
        super().__init__()
        self.pets_win = pets_win
        self.pet = pet
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Животные')
        self.setGeometry(630, 35, 300, 300)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('pictures/dog.png'))

        name_label = QLabel('Введите имя питомца:')
        self.name_input = QLineEdit()
        pet_species_label = QLabel('Введите вид питомца:')
        self.pet_species_input = QLineEdit()
        age_label = QLabel('Введите возраст питомца:')
        self.age_input = QLineEdit()
        weight_label = QLabel('Введите вес питомца:')
        self.weight_input = QLineEdit()
        self.save_btn = QPushButton('Сохранить')
        self.id = QLineEdit()
        self.save_btn.clicked.connect(self.save_pet)

        if self.pet:
            self.name_input.setText(self.pet['pet_name'])
            self.pet_species_input.setText(self.pet['animal_species'])
            self.age_input.setText(self.pet['age'])
            self.weight_input.setText(self.pet['weight'])
            self.id.setText(self.pet['id_pet'])

        main_l = QVBoxLayout()
        main_l.addWidget(name_label)
        main_l.addWidget(self.name_input)
        main_l.addWidget(pet_species_label)
        main_l.addWidget(self.pet_species_input)
        main_l.addWidget(age_label)
        main_l.addWidget(self.age_input)
        main_l.addWidget(weight_label)
        main_l.addWidget(self.weight_input)
        main_l.addStretch()
        main_l.addWidget(self.save_btn)
        self.setLayout(main_l)

    def save_pet(self):
        db = SessionLocal()
        pet_service = PetService(db)

        try:
            int(self.age_input.text())
            int(self.weight_input.text())

            if self.name_input.text() == '' or self.pet_species_input.text() == '' or self.age_input.text() == ''\
                    or self.weight_input.text() == '':
                QMessageBox.information(self, 'Информация',
                                        'Вы не заполнили все поля или заполнили их некорректно.')
            else:
                if self.id.text():
                    pet_service.update_pet(
                        id_pet=self.id.text(),
                        pet_name=self.name_input.text(),
                        animal_species=self.pet_species_input.text(),
                        age=self.age_input.text(),
                        weight=self.weight_input.text(),
                    )
                else:
                    pet_service.add_pet(
                        pet_name=self.name_input.text(),
                        animal_species=self.pet_species_input.text(),
                        age=self.age_input.text(),
                        weight=self.weight_input.text(),
                    )
                QMessageBox.information(self, 'Информация', 'Запись успешно сохранена!')
                self.close()
                self.pets_win.model.clear()
                self.pets_win.model.setHorizontalHeaderLabels(['id_pet', 'pet_name', 'animal_species', 'age', 'weight',
                                                               'home_status'])
                self.pets_win.load_orders()

        except ValueError:
            QMessageBox.information(self, 'Информация',
                                    'Вы не заполнили все поля или заполнили их некорректно.')
