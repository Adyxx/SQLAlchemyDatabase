from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.types import String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

SQLITE = 'sqlite'
MYSQL = 'mysql'

Base = declarative_base()

class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(length=50))
    animals = relationship('Animal', backref='type')


class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))
    type_fkey = Column(Integer, ForeignKey('types.id'))

class Database:
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
        MYSQL: 'mysql+mysqlconnector:///{USERNAME}:{PASSWORD}@localhost/{DB}'
    }

    def __init__(self, dbtype='sqlite', username='', password='', dbname='animals'):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname, USERNAME=username, PASSWORD=password)
            self.engine = create_engine(engine_url, echo=False)
        
        else:
            print('DBType is not found in DB_ENGINE')
        
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def read_all(self, order = Animal.name):
        try:
            result = self.session.query(Animal).order_by(order).all()
            return result
        except:
            return False

    def read_by_id(self, id):
        try:
            result = self.session.query(Animal).get(id)
            return result
        except:
            return False
    
    def read_by_type(self, typee='savci'):
        try:
            result = self.session.query(Animal).join(Type).filter(Type.full_name.like(f'%{typee}%')).order_by(Animal.name).all()
            return result
        except:
            return False
    
    def read_types(self):
        try:
            result = self.session.query(Type).all()
            return result
        except:
            return False
    
    def create(self, animal):
        try:
            self.session.add(animal)
            self.session.commit()
            return True
        except:
            return False

    def update(self):
        try:
            self.session.commit()
            return True
        except:
            return False
    
    def delete(self, id):
        try:
            animal = self.read_by_id(id)
            self.session.delete(animal)
            self.session.commit()
            return True
        except:
            return False

db = Database(dbtype='sqlite', dbname='animals.db')

#animalc = Animal()
#animalc.name = 'Liška polární'
#animalc.type_fkey = 1
#db.create(animalc)

animals = db.read_all()
for animal in animals:
    print(f'{animal.name} [{animal.type.full_name}]')

print('_____________')

if db.read_by_id(2):
    animall = db.read_by_id(2)
    animall.name = 'Želva nádherná'
    animall.type_fkey = 4
    db.update()
    

types = db.read_types()
for typeee in types:
    print(f'{typeee.full_name}')

print('_____________')

db.delete(2)

animals = db.read_all()
for animal in animals:
    print(f'{animal.name} [{animal.type.full_name}]')

print('_____________')


