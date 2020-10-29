import typing
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from src import rockemsocks

engine = db.create_engine('sqlite:///databases/rockemsocks.db')
Session = sessionmaker(bind=engine)


def queries() -> typing.Tuple[str, str]:
    """
    Return exactly one pairing of (FirstName, LastName) representing the person who:
    1. Made a purchase in the name of a company.
    2. Has his first name start with 'M'.
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
