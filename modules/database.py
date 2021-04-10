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

db = Database(dbtype='sqlite', dbname='animals.db')
animals = db.session.query(Animal).all()
for animal in animals:
    print(f'{animal.name} [{animal.type.id}]')
types = db.session.query(Type).all()
for typee in types:
    print(f'{typee.full_name} {typee.animals}')
