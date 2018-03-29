# project/server/models.py
'''
.. module:: models
    :synopsis; All the important classes
'''
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

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
    '''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


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
        relationship(User
    '''
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


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
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


engine = create_engine('postgresql://vagrant:vagrant@localhost/catalog')

Base.metadata.create_all(engine)
