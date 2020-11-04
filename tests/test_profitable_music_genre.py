import pytest
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from src import profitable_music_genre
from utils import rockemsocks


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)


@pytest.fixture(scope='module')
def db_session(db_engine: db.engine.Engine) -> db.orm.session.Session:
    return sessionmaker(bind=db_engine)


def test_most_profitable_music_genre(db_session: db.orm.session.Session) -> None:
    tested_result = [tuple(row) for row in profitable_music_genre.most_profitable_music_genre()]
    session = db_session()
    expected_result = [
        tuple(row)
        for row in (
            session.query(
                func.sum(rockemsocks.Tracks.UnitPrice).label('total_price'), rockemsocks.Genres.Name.label('genre_name')
            )
            .join(rockemsocks.Genres)
            .join(rockemsocks.InvoiceItem)
            .group_by(rockemsocks.Genres.GenreId)
            .order_by(db.desc('total_price'))
            .all()
        )
    ]
    assert len(tested_result) == len(expected_result)
    for tested, expected in zip(tested_result, expected_result):
        assert tested == expected
