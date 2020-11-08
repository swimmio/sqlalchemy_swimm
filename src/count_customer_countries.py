import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def count_customer_countries() -> int:
    """
    Return the number of countries that customers live in.
    Make sure that the number of countries is unique - no country should be counted twice.

    :return: Number of unique countries that customers live in.
    :rtype: int
    """
    session = Session()
    cust = rockemsocks.Customers
    return session.query(cust.CustomerId).group_by(cust.Country).count()
