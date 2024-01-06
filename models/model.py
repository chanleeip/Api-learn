from pydantic import BaseModel
from uuid import uuid4
from typing import Annotated,Union
from enum import Enum
from time import time

class Status (str,Enum):
    finished=True
    not_finished=False

class Gender(str,Enum):
    Male="male"
    female="female"
    
class Task(BaseModel):
    id:uuid4=uuid4()
    task_name:str
    status:Status
    task_description:str

class User(BaseModel):
    id:int
    first_name:str
    middle_name:Union[str , None]=None
    last_name:str
    date_created:time=time()