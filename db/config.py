from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL="postgresql://wbjhrcfk:Oh9-0QvWApeqi6OWNFirgsWeCBWH3_iE@tiny.db.elephantsql.com/wbjhrcfk"
engine = create_engine(DATABASE_URL)
Session=sessionmaker(bind=engine)
session=Session()

def get_session():
    return session