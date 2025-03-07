from datetime import date
from database import SessionLocal, init_db
from services.service import PetService, ParentService, ShelterService, WorkerService, EventService


def main():
    init_db()
    db = SessionLocal()

    try:
        pet_service = PetService(db)
        pet_service.add_pet(pet_name='Hog', animal_species='Pig', age=11, weight=56)
        pet_service.add_pet(pet_name='Bella', animal_species='Dog', age=3, weight=12)
        pet_service.add_pet(pet_name='Mittens', animal_species='Cat', age=2, weight=5)
        pet_service.add_pet(pet_name='Goldie', animal_species='Fish', age=1, weight=1)
        pet_service.add_pet(pet_name='Chirpy', animal_species='Parrot', age=4, weight=1)
        pet_service.add_pet(pet_name='Snowball', animal_species='Rabbit', age=5, weight=2)
        pet_service.add_pet(pet_name='Rocky', animal_species='Turtle', age=15, weight=3)
        pet_service.add_pet(pet_name='Shadow', animal_species='Dog', age=6, weight=18)
        pet_service.add_pet(pet_name='Whiskers', animal_species='Cat', age=7, weight=6)
        pet_service.add_pet(pet_name='Daisy', animal_species='Cow', age=8, weight=120)


        client_service = ParentService(db)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='SPB, Nevsky 12',
                                  passport_id=46456456)
        client_service.add_parent(name='Anna', surname='Petrova', phone_number=12345, address='Moscow, Lenina 5',
                                  passport_id=98765432)
        client_service.add_parent(name='Ivan', surname='Sidorov', phone_number=67890, address='SPB, Nevsky 10',
                                  passport_id=87654321)
        client_service.add_parent(name='Olga', surname='Smirnova', phone_number=11111, address='Kazan, Pobedy 3',
                                  passport_id=76543210)
        client_service.add_parent(name='Sergey', surname='Ivanov', phone_number=22222, address='Sochi, Mira 7',
                                  passport_id=65432109)
        client_service.add_parent(name='Dmitry', surname='Kuznetsov', phone_number=33333, address='Ufa, Gagarina 15',
                                  passport_id=54321098)
        client_service.add_parent(name='Tatiana', surname='Nikolaeva', phone_number=44444, address='Omsk, Pushkina 1',
                                  passport_id=43210987)
        client_service.add_parent(name='Vladimir', surname='Popov', phone_number=55555, address='Tomsk, Lermontova 9',
                                  passport_id=32109876)
        client_service.add_parent(name='Natalia', surname='Sokolova', phone_number=66666, address='Tver, Sovetskaya 12',
                                  passport_id=21098765)
        client_service.add_parent(name='Alexey', surname='Morozov', phone_number=77777, address='Penza, Kirova 6',
                                  passport_id=10987654)

        order_service = ShelterService(db)
        order_service.add_shelter(parent_name=1, pet_name=3)
        order_service.add_shelter(parent_name=2, pet_name=5)
        order_service.add_shelter(parent_name=3, pet_name=7)
        order_service.add_shelter(parent_name=4, pet_name=2)
        order_service.add_shelter(parent_name=5, pet_name=9)
        order_service.add_shelter(parent_name=9, pet_name=8)
        order_service.add_shelter(parent_name=10, pet_name=10)

        payment_service = WorkerService(db)
        payment_service.add_worker(name='Владимир', surname='Григорян', phone_number=32424234, login='Вова', password='123')

        event_service = EventService(db)
        event_service.add_event(event_name='Ягоды ляляля', event_date=date(2023, 6, 23))
        event_service.add_event(event_name='Музыкальный вечер', event_date=date(2023, 7, 1))
        event_service.add_event(event_name='Выставка собак', event_date=date(2023, 8, 15))
        event_service.add_event(event_name='Фестиваль уличной еды', event_date=date(2023, 9, 10))
        event_service.add_event(event_name='Концерт классической музыки', event_date=date(2023, 10, 5))
        event_service.add_event(event_name='Спортивный марафон', event_date=date(2023, 11, 20))
        event_service.add_event(event_name='Киноночь под открытым небом', event_date=date(2023, 12, 8))
        event_service.add_event(event_name='Театральная постановка', event_date=date(2024, 1, 14))
        event_service.add_event(event_name='Ярмарка ремесел', event_date=date(2024, 2, 22))
        event_service.add_event(event_name='Научная конференция', event_date=date(2024, 3, 30))

    finally:
        db.close()


if __name__ == '__main__':
    main()
