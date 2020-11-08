import typing

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def get_oldest_employees(count_employees: int) -> typing.List[typing.Tuple[str, str]]:
    """
    Return a list of pairs in the form of (FirstName, LastName).
    The list will consist of the `count` oldest employees from oldest to youngest.

    :param count: Number of employees to return.
    :type count: int
    :return: List of (FirstName, LastName) pairings from oldest to youngest.
    :rtype: typing.List[typing.Tuple[str, str]]
    """
    session = Session()
    empl = rockemsocks.Employees
    return (
        session.query(
            empl.FirstName,
            empl.LastName,
        )
        .order_by(db.asc(empl.BirthDate))
        .limit(count_employees)
        .all()
    )
