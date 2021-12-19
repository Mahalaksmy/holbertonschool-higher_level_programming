#!/usr/bin/python3
'''
Script that prints the first State object from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    md = create_engine.MetaData()
    Session = sessionmaker(bind=engine)

    session = Session()
    instance = session.query(State).first()

    if instance is not None:
        print('{}: {}'.format(instance.id, instance.name))
    else:
        print('Nothing')

    session.close()
