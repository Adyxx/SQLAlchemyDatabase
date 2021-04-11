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
    typee = Column(Integer, ForeignKey('types.id'))

class Info(Base):
    __tablename__ = 'infos'

    id = Column(Integer, primary_key=True)
    text = Column(String(length=200))
    info = Column(Integer, ForeignKey('types.id'))


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

    def read_animal_by_id(self, id):
        try:
            result = self.session.query(Animal).get(id)
            return result
        except:
            return False
    
    def read_type_by_id(self, typee):
        try:
            result = self.session.query(Typee).get(id)
            return result
        except:
            return False
    
    def read_info_by_id(self, info):
        try:
            result = self.session.query(Info).get(id)
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
    
    def update(self):
        try:
            self.session.commit()
            return True
        except:
            return False
    
    def create_animal(self, animal):
        try:
            self.session.add(animal)
            self.session.commit()
            return True
        except:
            return False
    
    def create_type(self, typee):
        try:
            self.session.add(typee)
            self.session.commit()
            return True
        except:
            return False
    
    def create_info(self, info):
        try:
            self.session.add(info)
            self.session.commit()
            return True
        except:
            return False
  
    def delete_animal(self, id):
        try:
            animal = self.read_animal_by_id(id)
            self.session.delete(animal)
            self.session.commit()
            return True
        except:
            return False

    def delete_type(self, id):
        try:
            typee = self.read_type_by_id(id)
            self.session.delete(typee)
            self.session.commit()
            return True
        except:
            return False
    
    def delete_info(self, id):
        try:
            info = self.read_info_by_id(id)
            self.session.delete(info)
            self.session.commit()
            return True
        except:
            return False


