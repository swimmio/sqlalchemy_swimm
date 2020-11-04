import pytest
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from src import queries
from utils import rockemsocks


@pytest.fixture(scope='module')
def db_engine() -> db.engine.Engine:
    return db.create_engine(rockemsocks.ROCKEMSOCKSDB_CONNECTION_STRING)


@pytest.fixture(scope='module')
def db_session(db_engine: db.engine.Engine) -> db.orm.session.Session:
    return sessionmaker(bind=db_engine)


def test_queries(db_session: db.orm.session.Session) -> None:
    session = db_session()
    tested_result = tuple(queries.queries())
    cust = rockemsocks.Customers
    expected_result = tuple(
        session.query(
            cust.FirstName,
            cust.LastName,
        )
        .filter((cust.Company != None) & (cust.FirstName.like('M%')))
        .one()
    )
    assert tested_result == expected_result
