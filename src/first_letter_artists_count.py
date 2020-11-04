import typing

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def get_first_letter_artists_count() -> typing.List[typing.Tuple[str, int]]:
    """
    Return a list of pairings describing how many artists start in each letter of the alphabet.
    The first member in this pairing will be called 'artist_first_letter' and is the first letter in which the names in this group start with (eg. 'A', 'D', 'Q').
    The second member in this pairing will be called 'count_artists' and is the number of artists who's name starts with that letter.
    The pairings are returned in a descending order according to the number of artists (most first, least last).
    Only pairings with a number of artists greater than 10 should be included in the returned list.
    """
    session = Session()
    first_letter_col = func.substr(rockemsocks.Artists.Name, 1, 1).label('artist_first_letter')
    count_artists_col = func.count(rockemsocks.Artists.ArtistId).label('count_artists')
    return (
        session.query(first_letter_col, count_artists_col)
        .group_by('artist_first_letter')
        .having(count_artists_col > 10)
        .order_by(db.desc('count_artists'))
        .all()
    )
