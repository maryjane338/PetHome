from database import SessionLocal, init_db
from services.service import PetService, ParentService, ShelterService, WorkerService, EventService


def main():
    init_db()
    db = SessionLocal()

    try:
        book_service = PetService(db)
        book_service.add_pet(pet_name='Hog', animal_species='Pig', age=11, weight=56, home_status='Не усыновлён')
        book_service.add_pet(pet_name='down', animal_species='Dog', age=3, weight=12, home_status='Не усыновлён')
        book_service.add_pet(pet_name='Idiot', animal_species='Parrot', age=2, weight=6, home_status='Не усыновлён')

        client_service = ParentService(db)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456)
        client_service.add_parent(name='dfg', surname='Tupodfgfgi', phone_number=546456, address='sdfgffffsfs', passport_id=46453556456)

        order_service = ShelterService(db)
        order_service.add_shelter(parent_name=1, pet_name=3)

        payment_service = WorkerService(db)
        payment_service.add_worker(name='dgeeg', surname='fefeew', phone_number=32424234, login='2234', password='234234')

        event_service = EventService(db)
        event_service.add_event(event_name='Ягоды ляляля', event_date=120660)
        event_service.add_event(event_name='Еживика ляляля', event_date=145830)
        event_service.add_event(event_name='Пёрд ляляля', event_date=120845)

    finally:
        db.close()


if __name__ == '__main__':
    main()
