from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import DeclarativeBase

import os

DB_PATH = "database/"

if not os.path.exists(DB_PATH):
   os.makedirs(DB_PATH)

DB_URL = 'sqlite:///%s/db.sqlite3' % DB_PATH

engine = create_engine(DB_URL, echo=False, convert_unicode=True)
Session = scoped_session(sessionmaker(autocommit=False,binds=engine))
Base = DeclarativeBase()