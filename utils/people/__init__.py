from .core import PEOPLEDB_META, hobbies, users
from .orm import Base, Hobbies, Users
from .orm_constraints import BaseCons, HobbiesCons, UsersCons

PEOPLEDB_CONNECTION_STRING = 'sqlite:///databases/people.db'
