from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from motor import motor_asyncio
from get_tender_backend.settings import settings
from sqlalchemy import MetaData

engine = create_engine(settings.sqlite_url)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

client = motor_asyncio.AsyncIOMotorClient(settings.mongo_url)
mongo_db = client.tender_db
