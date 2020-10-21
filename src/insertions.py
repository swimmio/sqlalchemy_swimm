import sqlalchemy as db


def data_insertions() -> None:
    """
    Insert to the previously created database two new people:
    - Homer Simpson, whose hobby is Beer.
    - Lisa Simpson, whose hobby is Saxophone.
    Note that you'll need to create entries in both the 'users' table and the 'hobbies' table.
    """
    engine = db.create_engine('sqlite:///databases/people.db')
    meta = db.MetaData()
    meta.reflect(bind=engine)
    users = meta.tables['users']
    hobbies = meta.tables['hobbies']

    with engine.connect() as connection:
        # Demonstrating single statement insertions
        homer_id: int = connection.execute(
            users.insert(
                {'first_name': 'Homer', 'last_name': 'Simpson'},
            ),
        ).inserted_primary_key[0]
        lisa_id: int = connection.execute(
            users.insert(
                {'first_name': 'Lisa', 'last_name': 'Simpson'},
            ),
        ).inserted_primary_key[0]
        # Demonstrating multiple statements generation
        connection.execute(
            hobbies.insert(), [{'hobby': 'Beer', 'user_id': homer_id}, {'hobby': 'Saxophone', 'user_id': lisa_id}]
        )
