from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./culture_sqlite.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True)

Base = declarative_base(name='Base')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
