from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from core.settings import DBSettings

# engine
db_settings = DBSettings()
engine = create_engine(db_settings.database_uri, echo=db_settings.echo)

SessionLocal = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=True,
        expire_on_commit=False,
    )
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
