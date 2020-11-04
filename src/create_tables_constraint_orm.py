import sqlalchemy as db
from utils import people


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
    engine = db.create_engine(people.PEOPLEDB_CONNECTION_STRING)
    people.BaseCons.metadata.create_all(engine)
