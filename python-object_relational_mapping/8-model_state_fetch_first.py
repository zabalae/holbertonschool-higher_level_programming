#!/usr/bin/python3
'''Script that prints the first State object'''


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    state = session.query(State).first()

    if state is not None:
        print("{}: {}".format(state.id, state.name))

    else:
        print("Nothing")

    session.close()
