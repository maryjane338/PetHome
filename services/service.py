from sqlalchemy.orm import Session
from models.db import Pet, Parent, Shelter, Worker, Event


class PetService:
    def __init__(self, db: Session):
        self.db = db

    def add_pet(self, pet_name: str, animal_species: str, age: int, weight: int):
        new_pet = Pet(
            pet_name=pet_name,
            animal_species=animal_species,
            age=age,
            weight=weight,
            home_status='Не усыновлён'
        )
        self.db.add(new_pet)
        self.db.commit()
        self.db.refresh(new_pet)
        return new_pet

    def update_pet(self, id_pet, pet_name, animal_species, age, weight):
        pet = self.db.query(Pet).filter_by(id_pet=id_pet).first()
        if pet:
            pet.id_pet = id_pet
            pet.pet_name = pet_name
            pet.animal_species = animal_species
            pet.age = age
            pet.weight = weight
            self.db.commit()
            self.db.refresh(pet)

    def delete_pet(self, id_pet):
        pet = self.db.query(Pet).filter_by(id_pet=id_pet).first()
        self.db.delete(pet)
        self.db.commit()

    def select_book_query(self, book_name):
        query_book = self.db.query(Book.id_book).filter_by(book_name=book_name).scalar()
        return query_book

    def select_book_name(self, book_name):
        query_book = self.db.query(Book.id_book).filter_by(book_name=book_name).scalar()
        return query_book

    def load_book(self, id_book):
        query_name = self.db.query(Book.book_name).filter_by(id_book=id_book).scalar()
        query_author = self.db.query(Book.author).filter_by(id_book=id_book).scalar()
        query_price = self.db.query(Book.price).filter_by(id_book=id_book).scalar()
        query_picture = self.db.query(Book.book_picture).filter_by(id_book=id_book).scalar()
        query = [query_name, query_author, query_price, query_picture]
        return query

    def selected_book(self, id_book):
        query_book = self.db.query(Book.book_name, Book.author, Book.book_picture, Book.price).\
            filter_by(id_book=id_book).scalar()
        query = [query_book]
        return query

    def get_all_pet(self):
        query = self.db.query(Pet).all()

        pets = []
        for b in query:
            pet = []
            pet.append(str(b.id_pet))
            pet.append(b.pet_name)
            pet.append(b.animal_species)
            pet.append(str(b.age))
            pet.append(str(b.weight))
            pet.append(b.home_status)
            pets.append(pet)
        return pets


class ParentService:
    def __init__(self, db: Session):
        self.db = db

    def add_parent(self, name: str,
                 surname: str, phone_number: int, address: str, passport_id: int):
        new_parent = Parent(
            name=name,
            surname=surname,
            phone_number=phone_number,
            address=address,
            passport_id=passport_id,
        )
        self.db.add(new_parent)
        self.db.commit()
        self.db.refresh(new_parent)
        return new_parent

    def update_parent(self, id_parent, name, surname, phone_number, address, passport_id):
        parent = self.db.query(Parent).filter_by(id_parent=id_parent).first()
        if parent:
            parent.id_parent = id_parent
            parent.name = name
            parent.surname = surname
            parent.phone_number = phone_number
            parent.address = address
            parent.passport_id = passport_id
            self.db.commit()
            self.db.refresh(parent)

    def delete_parent(self, id_parent):
        parent = self.db.query(Parent).filter_by(id_parent=id_parent).first()
        self.db.delete(parent)
        self.db.commit()

    def select_user_for_enter(self, user_name):
        user_password = self.db.query(Client.password).filter_by(client_name=user_name).scalar()
        return user_password

    def select_user(self, user_name):
        user_id = self.db.query(Client.id_client).filter_by(client_name=user_name).scalar()
        return user_id

    def get_all_pet(self):
        query = self.db.query(Parent).all()

        parents = []
        for c in query:
            parent = []
            parent.append(c.id_parent)
            parent.append(c.name)
            parent.append(c.surname)
            parent.append(c.phone_number)
            parent.append(c.address)
            parent.append(c.passport_id)
            parent.append(c.parent_status)
            parents.append(parent)
        return parents

    def get_all_parents(self):
        query = self.db.query(Parent).all()

        parents = []
        for b in query:
            parent = []
            parent.append(str(b.id_parent))
            parent.append(b.name)
            parent.append(b.surname)
            parent.append(str(b.phone_number))
            parent.append(str(b.address))
            parent.append(str(b.passport_id))
            parents.append(parent)
        return parents


class ShelterService:
    def __init__(self, db: Session):
        self.db = db

    def add_shelter(self, parent_name: int, pet_name: int):
        new_shelter = Shelter(
            parent_name=parent_name,
            pet_name=pet_name,
        )

        self.change_pet_status(pet_name)

        self.db.add(new_shelter)
        self.db.commit()
        self.db.refresh(new_shelter)
        return new_shelter

    def delete_shelter(self, id_shelter, pet_name):
        shelter = self.db.query(Shelter).filter_by(id_shelter=id_shelter).first()
        self.change_pet_status(pet_name)
        self.db.delete(shelter)
        self.db.commit()

    def change_pet_status(self, id_pet):
        pet = self.db.query(Pet).filter_by(id_pet=id_pet).first()
        if pet.home_status == 'Не усыновлён':
            pet.home_status = 'Усыновлён'
        else:
            pet.home_status = 'Не усыновлён'
        self.db.commit()
        self.db.refresh(pet)

    def update_shelter(self, id_shelter, parent_name, pet_name):
        shelter = self.db.query(Shelter).filter_by(id_shelter=id_shelter).first()
        if shelter:
            shelter.parent_name = parent_name
            shelter.pet_name = pet_name
            self.db.commit()
            self.db.refresh(shelter)

    def check_parent_and_pet(self, parent_name, pet_name):
        pet_query = self.db.query(Pet).filter_by(id_pet=pet_name).all()

        pets = []
        for b in pet_query:
            pet = []
            pet.append(str(b.id_pet))
            pet.append(b.pet_name)
            pet.append(b.animal_species)
            pet.append(str(b.age))
            pet.append(str(b.weight))
            pet.append(b.home_status)
            pets.append(pet)

        parent_query = self.db.query(Parent).filter_by(id_parent=parent_name).all()

        parents = []
        for b in parent_query:
            parent = []
            parent.append(str(b.id_parent))
            parent.append(b.name)
            parent.append(b.surname)
            parent.append(str(b.phone_number))
            parent.append(str(b.address))
            parent.append(str(b.passport_id))
            parents.append(parent)

        if len(pets) == 0 or len(parents) == 0:
            return 1
        elif len(pets) != 0:
            status = self.check_status(pet_name)
            if status == 1:
                return 1
        else:
            return 0

    def check_status(self, id_pet):
        pet = self.db.query(Pet).filter_by(id_pet=id_pet).first()
        print(pet.home_status)
        if pet.home_status == 'Усыновлён':
            return 1
        else:
            return 0

    def load_orders_for_user(self, id_user):
        query_id = self.db.query(Order.id_order).filter_by(client_name=id_user).all()
        ids = list(map(str, [id_order[0] for id_order in query_id]))

        query_book_id = self.db.query(Order.book_name).filter_by(client_name=id_user).all()
        books_ids = [book_id[0] for book_id in query_book_id]
        final_book_name = [
            self.db.query(Book.book_name).filter_by(id_book=book_id).scalar()
            for book_id in books_ids
        ]

        query_address = self.db.query(Order.address).filter_by(client_name=id_user).all()
        addresses = [address[0] for address in query_address]

        query_payment_id = self.db.query(Order.payment).filter_by(client_name=id_user).all()
        payment_ids = [payment_id[0] for payment_id in query_payment_id]
        final_payment_status = [
            self.db.query(Payment.payment_status).filter_by(id_payment=payment_id).scalar()
            for payment_id in payment_ids
        ]

        query_date = self.db.query(Order.delivery_date).filter_by(client_name=id_user).all()
        dates = [date[0] for date in query_date]

        loaded_orders = []

        for i in range(len(ids)):
            loaded_order = []
            loaded_order.append(ids[i - 1])
            loaded_order.append(final_book_name[i - 1])
            loaded_order.append(addresses[i - 1])
            loaded_order.append(final_payment_status[i - 1])
            loaded_order.append(dates[i - 1])
            loaded_orders.append(loaded_order)

        return loaded_orders

    def get_all_shelters(self):
        query = self.db.query(Shelter).all()

        shelters = []
        for o in query:
            shelter = []
            shelter.append(str(o.id_shelter))
            shelter.append(str(o.parent_name))
            shelter.append(str(o.pet_name))
            shelters.append(shelter)
        return shelters


class WorkerService:
    def __init__(self, db: Session):
        self.db = db

    def add_worker(self, name: str, surname: str, phone_number: int, login: str, password: str):
        new_worker = Worker(
            name=name,
            surname=surname,
            phone_number=phone_number,
            login=login,
            password=password,
        )
        self.db.add(new_worker)
        self.db.commit()
        self.db.refresh(new_worker)
        return new_worker

    def select_worker_for_enter(self, worker_login):
        worker_password = self.db.query(Worker.password).filter_by(login=worker_login).scalar()
        return worker_password


class EventService:
    def __init__(self, db: Session):
        self.db = db

    def add_event(self, event_name: str, event_date: str):
        new_event = Event(
            event_name=event_name,
            event_date=event_date,
        )
        self.db.add(new_event)
        self.db.commit()
        self.db.refresh(new_event)
        return new_event

    def update_event(self, id_event, event_name, event_date):
        event = self.db.query(Event).filter_by(id_event=id_event).first()
        if event:
            event.event_name = event_name
            event.event_date = event_date
            self.db.commit()
            self.db.refresh(event)

    def delete_event(self, id_event):
        event = self.db.query(Event).filter_by(id_event=id_event).first()
        self.db.delete(event)
        self.db.commit()

    def get_all_events(self):
        query = self.db.query(Event).all()

        events = []
        for p in query:
            event = []
            event.append(str(p.id_event))
            event.append(str(p.event_name))
            event.append(str(p.event_date))
            events.append(event)
        return events
