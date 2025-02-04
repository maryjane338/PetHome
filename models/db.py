from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base


class Pet(Base):
    __tablename__ = 'pets'

    id_pet = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pet_name = Column(String, nullable=False)
    animal_species = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    home_status = Column(Enum('Усыновлён', 'Не усыновлён', name='home_status_enum'), nullable=False)

    pet_ship = relationship('Shelter', back_populates='shelter_ship_pet')


class Parent(Base):
    __tablename__ = 'parents'

    id_parent = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    passport_id = Column(Integer, nullable=False)

    parent_ship = relationship('Shelter', back_populates='shelter_ship_parent')


class Shelter(Base):
    __tablename__ = 'shelters'

    id_shelter = Column(Integer, primary_key=True, index=True, autoincrement=True)
    parent_name = Column(Integer, ForeignKey('pets.id_pet'), nullable=False)
    pet_name = Column(Integer, ForeignKey('parents.id_parent'), nullable=False)

    shelter_ship_pet = relationship('Pet', back_populates='pet_ship')
    shelter_ship_parent = relationship('Parent', back_populates='parent_ship')


class Worker(Base):
    __tablename__ = 'workers'

    id_worker = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    login = Column(Integer, nullable=False)
    password = Column(String, nullable=False)


class Event(Base):
    __tablename__ = 'events'

    id_event = Column(Integer, primary_key=True, index=True, autoincrement=True)
    event_name = Column(String, nullable=False)
    event_date = Column(Integer, nullable=False)
