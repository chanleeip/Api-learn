from uuid import uuid4 
from typing import Union
from enum import Enum
from pydantic import BaseModel,Field

class Status (Enum):
    finished="finished"
    not_finished="not_finished"

class Gender(Enum):
    male="male"
    female="female"
    non_binary="non_binary"
    
class Priority(Enum):
    high_priority="high_priority"
    low_priority="low_priority"
    no_priority="no_priority"
class Task(BaseModel):
    task_name:str
    status:Status
    task_description:str
    priority:Priority
    due_date:str
    tags:list[str]=[]
    attachments:list[str]=[]

class User(BaseModel):
    username:Union[str , None]=None
    first_name:str
    middle_name:Union[str , None]=None
    last_name:str
    gender:Union[Gender,None]=None
