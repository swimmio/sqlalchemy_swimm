import sqlalchemy as db

PEOPLEDB_CONNECTION_STRING = 'sqlite:///databases/people.db'
PEOPLEDB_META = db.MetaData()

users = db.Table(
    'users',
    PEOPLEDB_META,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('first_name', db.String, nullable=False),
    db.Column('last_name', db.String, nullable=False),
)

hobbies = db.Table(
    'hobbies',
    PEOPLEDB_META,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('hobby', db.String, nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
)
