from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from model import Base

import os

DB_PATH = "database/"

if not os.path.exists(DB_PATH):
   os.makedirs(DB_PATH)

DB_URL = 'sqlite:///%s/db.sqlite3' % DB_PATH

engine = create_engine(DB_URL, echo=False)
Session = scoped_session(sessionmaker(binds=engine))

if not database_exists(engine.url):
    create_database(engine.url) 

Base.metadata.create_all(engine)