from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from backend.db import Base
# from Module_17.app.models.task import Task


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    # tasks = relationship('Task', back_populates='user')
    # создает ошибки если пытаться обратиться к таблице


if __name__ == '__main__':
    CreateTable(User.__table__)
