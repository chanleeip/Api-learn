from sqlalchemy import Column,Table,Integer,PrimaryKeyConstraint,create_engine,MetaData

from databases import Database

DATABASE_URL="postgresql://nithinn:Chunkymani@01@localhost/task_management"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
print(engine)