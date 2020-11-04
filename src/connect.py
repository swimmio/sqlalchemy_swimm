import typing

import sqlalchemy as db


def connect_to_helloworldb() -> typing.List[str]:
    """
    Connect to 'helloworldb' and return the names of all the tables there.

    :return: Names of the tables in the connected DB.
    :rtype: typing.List[str]
    """
    engine = db.create_engine('sqlite:///databases/helloworldb.db')
    return engine.table_names()
