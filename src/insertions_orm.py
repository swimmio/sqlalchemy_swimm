import sqlalchemy as db
from utils import people
from sqlalchemy.orm import sessionmaker

engine = db.create_engine(people.PEOPLEDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def data_insertions_orm() -> None:
    """
    Insert to the previously created database two new people using the SQLAlchemy ORM:
    - Homer Simpson, who's hobby is Beer.
    - Lisa Simpson, who's hobby is Saxophone.
    Note that you'll need to create entries in both the 'users' table and the 'hobbies' table.
    """
    session = Session()

    user_homer = people.Users(first_name='Homer', last_name='Simpson')
    user_lisa = people.Users(first_name='Lisa', last_name='Simpson')
    session.add_all([user_homer, user_lisa])
    session.commit()

    hobby_homer = people.Hobbies(hobby='Beer', user_id=user_homer.id)
    hobby_lisa = people.Hobbies(hobby='Saxophone', user_id=user_lisa.id)
    session.add_all([hobby_homer, hobby_lisa])
    session.commit()
