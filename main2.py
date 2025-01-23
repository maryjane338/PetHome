from database import SessionLocal, init_db
from services.service import PetService, ParentService, ShelterService, WorkerService


def main():
    init_db()
    db = SessionLocal()

    try:
        book_service = PetService(db)
        book_service.add_pet(pet_name='Hog', animal_species='Pig', age=11, weight=56)
        book_service.add_pet(pet_name='down', animal_species='Dog', age=3, weight=12)

        client_service = ParentService(db)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='Lexa', surname='Tupoi', phone_number=6657, address='sdfsfs', passport_id=46456456, parent_status='ok',)
        client_service.add_parent(name='dfg', surname='Tupodfgfgi', phone_number=546456, address='sdfgffffsfs', passport_id=46453556456, parent_status='okhhghh',)

        order_service = ShelterService(db)
        order_service.add_shelter(parent_name=1, pet_name=2)

        payment_service = WorkerService(db)
        payment_service.add_worker(name='dgeeg', surname='fefeew', phone_number=32424234, login='2234', password='234234')


    finally:
        db.close()


if __name__ == '__main__':
    main()
