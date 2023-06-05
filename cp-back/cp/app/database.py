from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DB_URL = 'mysql+pymysql://cp:1234@localhost:3306/cp'
engine = create_engine(DB_URL)


def get_db_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
