import pytest
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from src import first_letter_artists_count
from utils import rockemsocks


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)


@pytest.fixture(scope='module')
def db_session(db_engine: db.engine.Engine) -> db.orm.session.Session:
    return sessionmaker(bind=db_engine)


def test_get_first_letter_artists_count(db_session: db.orm.session.Session) -> None:
    tested_result = [tuple(row) for row in first_letter_artists_count.get_first_letter_artists_count()]
    session = db_session()
    first_letter_col = func.substr(rockemsocks.Artists.Name, 1, 1).label('artist_first_letter')
    count_artists_col = func.count(rockemsocks.Artists.ArtistId).label('count_artists')
    expected_result = [
        tuple(row)
        for row in (
            session.query(first_letter_col, count_artists_col)
            .group_by('artist_first_letter')
            .having(count_artists_col > 10)
            .order_by(db.desc('count_artists'))
            .all()
        )
    ]
    assert len(tested_result) == len(expected_result)
    for tested, expected in zip(tested_result, expected_result):
        assert tested == expected
