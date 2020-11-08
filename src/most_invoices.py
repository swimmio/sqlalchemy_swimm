import typing

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def get_city_with_most_invoices() -> typing.Tuple[str, int]:
    """
    Return a single pair of (BillingCity, `Count`) where `Count` is the number of invoices attributed to that city.
    The pair should hold the name of the city with the highest invoices count as well as the count itself.

    :return: Single pair of (BillingCity, `Count`) representing the city with the most invoices.
    :rtype: typing.Tuple[str, int]
    """
    session = Session()
    inv = rockemsocks.Invoice
    count_subquery = (
        session.query(inv.BillingCity.label('city'), db.func.count(inv.BillingCity).label('count'))
        .group_by(inv.BillingCity)
        .subquery()
    )
    return session.query(db.func.max(count_subquery.c.count), count_subquery.c.city).one()
