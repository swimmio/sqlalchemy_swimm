import sqlalchemy as db
from .orm import *

ROCKEMSOCKSDB_CONNECTION_STRING = 'sqlite:///databases/rockemsocks.db'
ROCKEMSOCKSDB_META = db.MetaData()
