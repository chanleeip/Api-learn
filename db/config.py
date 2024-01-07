import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL=os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Session=sessionmaker(bind=engine)
session=Session()

def get_session():
    return session