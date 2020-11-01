import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('sqlite:///databases/people.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Users(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)


class Hobbies(Base):
    __tablename__ = 'hobbies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hobby = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


def data_insertions_orm() -> None:
    """
    Insert to the previously created database two new people using the SQLAlchemy ORM:
    - Homer Simpson, who's hobby is Beer.
    - Lisa Simpson, who's hobby is Saxophone.
    Note that you'll need to create entries in both the 'users' table and the 'hobbies' table.
    """
    session = Session()

    user_homer = Users(first_name='Homer', last_name='Simpson')
    user_lisa = Users(first_name='Lisa', last_name='Simpson')
    session.add_all([user_homer, user_lisa])
    session.commit()

    hobby_homer = Hobbies(hobby='Beer', user_id=user_homer.id)
    hobby_lisa = Hobbies(hobby='Saxophone', user_id=user_lisa.id)
    session.add_all([hobby_homer, hobby_lisa])
    session.commit()
