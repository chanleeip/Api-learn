from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL="postgresql://nithinn:Chunkymani01@localhost:5432/task_management"
engine = create_engine(DATABASE_URL)
Session=sessionmaker(bind=engine)
session=Session()

def get_session():
    return session