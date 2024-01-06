from sqlalchemy import Column, Integer, String, ForeignKey, Date,MetaData,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

DATABASE_URL="postgresql://nithinn:Chunkymani@01@localhost/task_management"
engine = create_engine(DATABASE_URL)
Session=sessionmaker(bind=engine)
session=Session()
metadata = Base.MetaData()

class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    first_name=Column(String(30),nullable=False)
    last_name=Column(String(30),nullable=False)
    middle_name=Column(String(30),nullable=True)
    date_created=Column(Date,nullable=False)

