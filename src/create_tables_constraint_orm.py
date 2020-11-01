import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import CheckConstraint, UniqueConstraint


def create_tables_constraints_orm() -> None:
    """
    Create the following tables using the SQLAlchemy ORM in a database called `people.db` (located in `./databases/people.db`):
    - 'users' table with the following fields:
        * 'id': integer, primary key, autoincremented
        * 'first_name': string, not nullable
        * 'last_name': string, not nullable, should have a CHECK CONSTRAINT telling it to only accept the 'Simpson' surname (named 'simpson_clause')
        * A UNIQUE CONSTRAINT that's places as a composite of both the first and the last name (named 'unique_name_clause')
    - 'hobbies' table with the following fields:
        * 'id': integer, primary key, autoincremented
        * 'hobby': string, not nullable, INDEXED (index name: 'ix_hobbies_hobby')
        * 'user_id': integer, foreign key connected to 'users' table 'id' column
    """
    engine = db.create_engine('sqlite:///databases/people.db')
    Base = declarative_base()

    class Users(Base):
        __tablename__ = 'users'
        __table_args__ = (
            CheckConstraint('last_name == "Simpson"', name='simpson_clause'),
            UniqueConstraint('first_name', 'last_name', name='unique_name_clause'),
        )
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        first_name = db.Column(db.String, nullable=False)
        last_name = db.Column(db.String, nullable=False)

    class Hobbies(Base):
        __tablename__ = 'hobbies'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        hobby = db.Column(db.String, nullable=False, index=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    Base.metadata.create_all(engine)
