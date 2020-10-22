import pytest
import sqlalchemy as db
from src import selections


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine('sqlite:///databases/rockemsocks.db')


@pytest.fixture(scope='module')
def db_meta() -> db.MetaData:
    return db.MetaData()


@pytest.mark.parametrize(
    'min_time, min_bytes',
    [(10 * 60 * 1000, 500 * 1024 * 1024), (5 * 60 * 1000, 50 * 1024 * 1024), (2 * 60 * 1000, 100 * 1024 * 1024)],
)
def test_selections(db_engine: db.engine.Engine, db_meta: db.MetaData, min_time: int, min_bytes: int) -> None:
    code_returned_rows = [tuple(row) for row in selections.selections(min_time, min_bytes)]
    db_meta.reflect(bind=db_engine)
    tracks = db_meta.tables['tracks']

    with db_engine.connect() as connection:
        clause = (tracks.c.Milliseconds > min_time) & (tracks.c.Bytes > min_bytes)
        query = db.select([tracks.c.TrackId]).where(clause)
        results = [tuple(row) for row in connection.execute(query).fetchall()]

    assert len(results) == len(code_returned_rows)
    for test_result, selection_result in zip(results, code_returned_rows):
        assert test_result == selection_result
