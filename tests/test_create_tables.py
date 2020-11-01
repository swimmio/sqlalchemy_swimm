import pytest
import sqlalchemy as db
from sqlalchemy.engine import reflection
from src import create_tables, create_tables_orm

MODE_CORE = 'core'
MODE_ORM = 'orm'


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine('sqlite:///databases/people.db')


@pytest.fixture(scope='module')
def db_meta() -> db.MetaData:
    return db.MetaData()


@pytest.fixture(scope='module')
def db_inspector(db_engine: db.engine.Engine) -> reflection.Inspector:
    return db.inspect(db_engine)


def delete_db_structure(db_engine: db.engine.Engine, db_meta: db.MetaData) -> None:
    db_meta.reflect(bind=db_engine)
    db_meta.drop_all(bind=db_engine)


@pytest.mark.parametrize('mode', [MODE_CORE, MODE_ORM])
def test_tables(
    mode: str, db_engine: db.engine.Engine, db_meta: db.MetaData, db_inspector: reflection.Inspector
) -> None:
    delete_db_structure(db_engine, db_meta)
    if mode == MODE_CORE:
        create_tables.create_tables()
    if mode == MODE_ORM:
        create_tables_orm.create_tables_orm()
    users_table_check(db_inspector)
    hobbies_table_check(db_inspector)


def users_table_check(db_inspector: reflection.Inspector) -> None:
    cols = [col['name'] for col in db_inspector.get_columns('users')]
    assert sorted(cols) == sorted(['id', 'first_name', 'last_name'])


def hobbies_table_check(db_inspector: reflection.Inspector) -> None:
    cols = [col['name'] for col in db_inspector.get_columns('hobbies')]
    assert sorted(cols) == sorted(['id', 'hobby', 'user_id'])
    foreign = db_inspector.get_foreign_keys('hobbies')
    assert len(foreign) == 1
    assert foreign[0]['constrained_columns'] == ['user_id']
    assert foreign[0]['referred_columns'] == ['id']
    assert foreign[0]['referred_table'] == 'users'
