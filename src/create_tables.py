import sqlalchemy as db
from utils import people


def create_tables() -> None:
    """
    Create the following tables in a database called `people.db` (located in `./databases/people.db`):
    - 'users' table with the following fields:
        * 'id': integer, primary key, autoincremented
        * 'first_name': string, not nullable
        * 'last_name': string, not nullable
    - 'hobbies' table with the following fields:
        * 'id': integer, primary key, autoincremented
        * 'hobby': string, not nullable
        * 'user_id': integer, foreign key connected to 'users' table 'id' column
    """
    engine = db.create_engine(people.PEOPLEDB_CONNECTION_STRING)
    people.PEOPLEDB_META.create_all(engine)
