import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


def create_tables_orm() -> None:
    """
    Create the following tables using the SQLAlchemy ORM in a database called `people.db` (located in `./databases/people.db`):
    - 'users' table with the following fields:
        * 'id': integer, primary key, autoincremented
        * 'first_name': string, not nullable
        * 'last_name': string, not nullable
    - 'hobbies' table with the following fields:
        * 'id': integer, primary key, autoincremented
        * 'hobby': string, not nullable
        * 'user_id': integer, foreign key connected to 'users' table 'id' column
    """
    engine = db.create_engine('sqlite:///databases/people.db')
    Base = declarative_base()

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

    Base.metadata.create_all(engine)
