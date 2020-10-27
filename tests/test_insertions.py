import pytest
import sqlalchemy as db
from sqlalchemy.engine import reflection
from src import insertions, insertions_orm

MODE_CORE = 'core'
MODE_ORM = 'orm'


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine('sqlite:///databases/people.db')


@pytest.fixture(scope='module')
def db_inspector(db_engine: db.engine.Engine) -> reflection.Inspector:
    return db.inspect(db_engine)


@pytest.fixture(scope='module')
def db_meta() -> db.MetaData:
    return db.MetaData()


@pytest.mark.parametrize('mode', [MODE_CORE, MODE_ORM])
def test_insertions(mode: str, db_engine: db.engine.Engine, db_meta: db.MetaData) -> None:
    db_meta.reflect(bind=db_engine)
    truncate_tables(db_engine, db_meta)
    if mode == MODE_CORE:
        insertions.data_insertions()
        pass
    elif mode == MODE_ORM:
        insertions_orm.data_insertions_orm()
        pass
    users = db_meta.tables['users']
    hobbies = db_meta.tables['hobbies']
    with db_engine.connect() as connection:
        results = sorted(
            connection.execute(
                db.select([users.c.first_name, users.c.last_name, hobbies.c.hobby]).select_from(users.join(hobbies))
            ).fetchall(),
            key=lambda row: row['first_name'],
        )
    homer_result = results[0]
    lisa_result = results[1]
    assert homer_result['first_name'] == 'Homer'
    assert homer_result['last_name'] == 'Simpson'
    assert homer_result['hobby'] == 'Beer'
    assert lisa_result['first_name'] == 'Lisa'
    assert lisa_result['last_name'] == 'Simpson'
    assert lisa_result['hobby'] == 'Saxophone'


def truncate_tables(db_engine: db.engine.Engine, db_meta: db.MetaData) -> None:
    with db_engine.connect() as connection:
        for table in db_meta.sorted_tables:
            connection.execute(table.delete())
