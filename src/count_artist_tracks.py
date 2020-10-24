import sqlalchemy as db
from sqlalchemy.sql import func


def count_artist_tracks(artist_name: str) -> int:
    """
    Return how many tracks does a certain artist has in the database.

    :param artist_name: the artist to query about.
    :type artist_name: str
    :return: number of tracks the artist has.
    :rtype: int
    """
    engine = db.create_engine('sqlite:///databases/rockemsocks.db')
    meta = db.MetaData()
    meta.reflect(bind=engine)
    tracks = meta.tables['tracks']
    albums = meta.tables['albums']
    artists = meta.tables['artists']

    with engine.connect() as connection:
        clause = artists.c.Name == artist_name
        joined_tables = tracks.join(albums).join(artists)
        query = db.select([func.count(tracks.c.TrackId).label('count')]).select_from(joined_tables).where(clause)
        results = connection.execute(query).fetchall()

    return results[0].count
