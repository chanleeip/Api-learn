from uuid import uuid4 
from typing import Union
from enum import Enum
from pydantic import BaseModel,Field

class Status (str,Enum):
    finished=True
    not_finished=False

class Gender(Enum):
    male="male"
    female="female"
    non_binary="non_binary"
    
class Task(BaseModel):
    id:uuid4=Field(default_factory=uuid4)
    task_name:str
    status:Status
    task_description:str

class User(BaseModel):
    user_name:str
    first_name:str
    middle_name:Union[str , None]=None
    last_name:str
    gender:Gender
