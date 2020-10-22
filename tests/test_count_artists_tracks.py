import pytest
import sqlalchemy as db
from sqlalchemy.sql import func
from sqlalchemy.sql.functions import count
from src import count_artist_tracks


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine('sqlite:///databases/rockemsocks.db')


@pytest.fixture(scope='module')
def db_meta() -> db.MetaData:
    return db.MetaData()


@pytest.mark.parametrize('artist_name', ['Foo Fighters', 'AC/DC', 'Queen'])
def test_insertions(db_engine: db.engine.Engine, db_meta: db.MetaData, artist_name: str) -> None:
    count_tracks = count_artist_tracks.count_artist_tracks(artist_name)
    db_meta.reflect(bind=db_engine)
    tracks = db_meta.tables['tracks']
    albums = db_meta.tables['albums']
    artists = db_meta.tables['artists']

    with db_engine.connect() as connection:
        clause = artists.c.Name == artist_name
        joined_tables = tracks.join(albums).join(artists)
        query = db.select([func.count(tracks.c.TrackId).label('count')]).select_from(joined_tables).where(clause)
        results = connection.execute(query).fetchall()

    count_tracks_test = results[0].count
    assert count_tracks == count_tracks_test
