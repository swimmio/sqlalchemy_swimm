import sqlalchemy as db


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
    engine = db.create_engine('sqlite:///databases/people.db')
    meta = db.MetaData()
    users = db.Table(
        'users',
        meta,
        db.Column('id', db.Integer, primary_key=True, autoincrement=True),
        db.Column('first_name', db.String, nullable=False),
        db.Column('last_name', db.String, nullable=False),
    )
    hobbies = db.Table(
        'hobbies',
        meta,
        db.Column('id', db.Integer, primary_key=True, autoincrement=True),
        db.Column('hobby', db.String, nullable=False),
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    )
    meta.create_all(engine)
