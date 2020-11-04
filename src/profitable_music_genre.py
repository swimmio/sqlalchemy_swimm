import decimal
import typing

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def most_profitable_music_genre() -> typing.List[typing.Tuple[decimal.Decimal, str]]:
    """
    Return a list of pairings describing the total value of all invoices per genre.
    The first member in this pairing is called 'total_price' and it's the sum of all the orders that were made.
    The second member in this pairing is called 'genre_name' and it's the musical genre for which we're counting the profits.
    The pairings are returned in a descending order according to the their total price.
    """
    session = Session()
    return (
        session.query(
            func.sum(rockemsocks.Tracks.UnitPrice).label('total_price'), rockemsocks.Genres.Name.label('genre_name')
        )
        .join(rockemsocks.Genres)
        .join(rockemsocks.InvoiceItem)
        .group_by(rockemsocks.Genres.GenreId)
        .order_by(db.desc('total_price'))
        .all()
    )
