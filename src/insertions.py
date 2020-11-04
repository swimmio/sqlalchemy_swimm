import sqlalchemy as db
from utils import people


def data_insertions() -> None:
    """
    Insert to the previously created database two new people:
    - Homer Simpson, who's hobby is Beer.
    - Lisa Simpson, who's hobby is Saxophone.
    Note that you'll need to create entries in both the 'users' table and the 'hobbies' table.
    """
    engine = db.create_engine(people.PEOPLEDB_CONNECTION_STRING)

    with engine.connect() as connection:
        # Demonstrating single statement insertions
        homer_id: int = connection.execute(
            people.users.insert(
                {'first_name': 'Homer', 'last_name': 'Simpson'},
            ),
        ).inserted_primary_key[0]
        lisa_id: int = connection.execute(
            people.users.insert(
                {'first_name': 'Lisa', 'last_name': 'Simpson'},
            ),
        ).inserted_primary_key[0]
        # Demonstrating multiple statements generation
        connection.execute(
            people.hobbies.insert(),
            [{'hobby': 'Beer', 'user_id': homer_id}, {'hobby': 'Saxophone', 'user_id': lisa_id}],
        )
