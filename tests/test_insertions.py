import pytest
import sqlalchemy as db
from sqlalchemy.engine import reflection
from src import insertions


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine('sqlite:///databases/people.db')


@pytest.fixture(scope='module')
def db_inspector(db_engine: db.engine.Engine) -> reflection.Inspector:
    return db.inspect(db_engine)


@pytest.fixture(scope='module')
def db_meta() -> db.MetaData:
    return db.MetaData()


def test_insertions(db_engine: db.engine.Engine, db_meta: db.MetaData, db_inspector: reflection.Inspector) -> None:
    insertions.data_insertions()
    db_meta.reflect(bind=db_engine)
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
    assert homer_result['hobby'] == 'Beer'
    assert lisa_result['first_name'] == 'Lisa'
    assert lisa_result['hobby'] == 'Saxophone'
