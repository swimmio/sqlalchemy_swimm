import typing

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def something_like() -> typing.Tuple[str, str]:
    """
    Return exactly one pairing of (FirstName, LastName) representing the person who:
    1. Made a purchase in the name of a company.
    2. Their first name starts with 'M'.
    """
    session = Session()
    cust = rockemsocks.Customers
    return (
        session.query(
            cust.FirstName,
            cust.LastName,
        )
        .filter((cust.Company != None) & (cust.FirstName.like('M%')))
        .one()
    )
