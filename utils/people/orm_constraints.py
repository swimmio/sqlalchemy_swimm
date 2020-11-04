import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import CheckConstraint, UniqueConstraint

BaseCons = declarative_base()


class UsersCons(BaseCons):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint('last_name == "Simpson"', name='simpson_clause'),
        UniqueConstraint('first_name', 'last_name', name='unique_name_clause'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)


class HobbiesCons(BaseCons):
    __tablename__ = 'hobbies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hobby = db.Column(db.String, nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
