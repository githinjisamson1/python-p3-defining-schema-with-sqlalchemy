#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# !data models/models == classes
class Student(Base):
    # !name of sql database table
    __tablename__ = 'students'
    
    # !attributes/fields
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    

if __name__ == '__main__':
    '''
    Refactoring any scripted elements of our modules to fit into this block makes sure that the script only runs when we tell it to.
    '''
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

# !persisting schemas
'''
The create_all() command on the next line tells the engine that any models that were created using Base as a parent should be used to create tables.
'''
# engine = create_engine('sqlite:///students.db')
# Base.metadata.create_all(engine)

'''
chmod +x lib/sqlalchemy_sandbox.py
python3 lib/sqlalchemy_sandbox.py
'''