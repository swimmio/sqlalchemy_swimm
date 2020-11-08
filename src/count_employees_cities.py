import typing

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from utils import rockemsocks

engine = db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)


def count_employees_cities() -> typing.List[typing.Tuple[str, str]]:
    """
    Return pairings consisting of (City, `Count`) where `Count` is the number of employees who live in that city.
    The pairings will be returned in a descending order, from least employees to most employees.

    :return: List of (City, `Count`) pairings in a descending order according to `Count`.
    :rtype: typing.List[typing.Tuple[str, str]]
    """
    session = Session()
    empl = rockemsocks.Employees
    return (
        session.query(empl.City, db.func.count(empl.EmployeeId).label('count'))
        .group_by(empl.City)
        .order_by(db.desc('count'))
        .all()
    )
