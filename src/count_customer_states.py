import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def count_usa_customer_states() -> int:
    """
    Return the number of USA States that customers live in.
    Make sure that the number of States is unique - no State should be counted twice.

    :return: Number of unique States that customers in the USA live in.
    :rtype: int
    """
    session = Session()
    cust = rockemsocks.Customers
    return session.query(cust.CustomerId).filter(cust.Country == 'USA').group_by(cust.State).count()
