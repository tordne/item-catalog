# project/server/models.py
'''
.. module:: models
    :synopsis; All the important classes
'''
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import create_engine

import os

Base = declarative_base()


class User(Base):
    '''
    The User class contains 3 attributes id, name, email

    .. py:attribute:: id
        Integer, primary_key=True
    .. py:attribute:: name
        String(250), nullable=False
    .. py:attribute:: email
        String(250), nullable=False
    .. py:attribute:: google_id
        String(30), nullable=False
    '''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    google_id = Column(String(30), nullable=False)


class Category(Base):
    '''
    The Category class has has 2 basic attributes id, name
    The 3rd attribute is the relationship with 'User' table

    .. py:attribute:: id
        Integer, primary_key=True
    .. py:attribute:: name
        String(250), nullable=False
    .. py:attribute:: user_id
        Integer, ForeignKey('user.id')
    .. py:attribute:: user
        relationship(User)

    .. py:attribute:: items
        relationship("Item", cascade="save-update, merge, delete")
    '''
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    items = relationship("Item", cascade="save-update, merge, delete")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
        }


class Item(Base):
    '''
    The Item class has 3 basic attr. id, name, description
    The 3rd and 4th attr. are relationships to the User and Category tables

    .. py:attribute:: id
        Integer, primary_key=True
    .. py:attribute:: name
        String(250), nullable=False
    .. py:attribute:: description
        String(250)
    .. py:attribute:: date_time
        DateTime, nullable=False, default=datetime.utcnow()

    .. py:attribute:: category_id
        Integer, ForeignKey('category.id')
    .. py:attribute:: category
        relationship(Category)

    .. py:attribute:: user_id
        Integer, ForeignKey('user.id')
    .. py:attribute:: user
        relationship(User
    '''
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    date_time = Column(DateTime,
                       nullable=False,
                       server_default=func.now(),
                       onupdate=func.now())

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date_time': self.date_time,
            'category_id': self.category_id,
            'user_id': self.user_id,
        }


class Credential(Base):
    '''
    This Authentication class contains the authentication token and credentials.

    .. py:attribute:: id
        Integer, primary_key=True
    .. py:attribute:: cred_token
        String(150), nullable=False
    .. py:attribute:: cred_expiry
        DateTime, nullable=False
    .. py:attribute:: cred_refresh
        String(150), nullable=False

    .. py:attribute:: user_id
        Integer, ForeignKey('user.id')
    .. py:attribute:: user
        relationship(User
    '''
    __tablename__ = 'credential'

    id = Column(Integer, primary_key=True)
    cred_token = Column(String(150), nullable=False)
    cred_expiry = Column(DateTime, nullable=False)
    cred_refresh = Column(String(150), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


engine = create_engine(os.environ['DATABASE_URL'])

Base.metadata.create_all(engine)
