from sqlalchemy import Column, Integer, String, ForeignKey, Sequence,create_engine,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

Base=declarative_base()

DATABASE_URL="postgresql://nithinn:Chunkymani01@localhost:5432/task_management"
engine = create_engine(DATABASE_URL)
Session=sessionmaker(bind=engine)
session=Session()

class Users(Base):
    __tablename__='users'
    id_sec = Sequence(__tablename__ + "_id_seq")
    id=Column(Integer, id_sec, server_default=id_sec.next_value(),nullable=False)
    uuid=Column(UUID(as_uuid=True),default=uuid.uuid4,autoincrement=False,primary_key=True)
    user_name=Column(String(30),nullable=False,unique=True)
    first_name=Column(String(30),nullable=False)
    last_name=Column(String(30),nullable=False)
    middle_name=Column(String(30),nullable=True)
    date_created=Column(TIMESTAMP(timezone=False),default=datetime.now())

Base.metadata.create_all(bind=engine)
