import sqlite3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


# объект Engine, который объект Session будет использован для
# соединения с ресурсами
engine = create_engine('sqlite:///js_event', echo=False)
Session = sessionmaker(bind=engine)     # создание конфигурации класса Session
s = Session()                           # создание объекта Session


Base = declarative_base()


class Events(Base):
    __tablename__ = 'js_event'

    id = Column(Integer, primary_key=True)
    name = Column(String(), index=True)
    date = Column(String(), index=True, unique=True)
    link = Column(String(), unique=True)

    def __repr__(self):
        return '<Events %r>' % self.name


Base.metadata.create_all(engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
