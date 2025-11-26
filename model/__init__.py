from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .base import Base
from .comment import Comment

import os

# Path to the database directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.dirname(BASE_DIR)

DB_PATH = os.path.join(PARENT_DIR, "database")

if not os.path.exists(DB_PATH):
   os.makedirs(DB_PATH)

DB_URL = 'sqlite:///%s/db.sqlite3' % DB_PATH

engine = create_engine(DB_URL, echo=True)
Session = scoped_session(sessionmaker(bind=engine))

if not database_exists(engine.url):
    create_database(engine.url) 

Base.metadata.create_all(engine)