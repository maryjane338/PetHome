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
