import os

import pytest
import sqlalchemy as db
from sqlalchemy.engine import reflection
from src import create_tables


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine('sqlite:///databases/people.db')


@pytest.fixture(scope='module')
def db_inspector(db_engine: db.engine.Engine) -> reflection.Inspector:
    return db.inspect(db_engine)


@pytest.fixture(scope='module')
def db_meta() -> db.MetaData:
    return db.MetaData()


def setup_function():
    os.unlink('./databases/people.db')
    create_tables.create_tables()


def test_users_table(db_engine: db.engine.Engine, db_meta: db.MetaData, db_inspector: reflection.Inspector) -> None:
    cols = [col['name'] for col in db_inspector.get_columns('users')]
    assert sorted(cols) == sorted(['id', 'first_name', 'last_name'])


def test_hobbies_table(db_engine: db.engine.Engine, db_inspector: reflection.Inspector) -> None:
    cols = [col['name'] for col in db_inspector.get_columns('hobbies')]
    assert sorted(cols) == sorted(['id', 'hobby', 'user_id'])
    foreign = db_inspector.get_foreign_keys('hobbies')
    assert len(foreign) == 1
    assert foreign[0]['constrained_columns'] == ['user_id']
    assert foreign[0]['referred_columns'] == ['id']
    assert foreign[0]['referred_table'] == 'users'
