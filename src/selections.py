import typing

import sqlalchemy as db


def selections(min_time: int, min_bytes: int) -> typing.List[db.engine.RowProxy]:
    """
    Return all tracks who're longer than `min_time` milliseconds and take more space than `min_bytes` bytes.

    :param min_time: minimum time in milliseconds.
    :type min_time: int
    :param min_bytes: minimum size in bytes.
    :type min_bytes: int
    :return: All the rows (as sqlalchemy returns them)  who fir the criteria.
    :rtype: typing.List[db.engine.RowProxy]
    """
    engine = db.create_engine('sqlite:///databases/rockemsocks.db')
    meta = db.MetaData()
    meta.reflect(bind=engine)
    tracks = meta.tables['tracks']

    with engine.connect() as connection:
        clause = (tracks.c.Milliseconds > min_time) & (tracks.c.Bytes > min_bytes)
        query = db.select([tracks.c.TrackId]).where(clause)
        results = connection.execute(query).fetchall()

    return results
