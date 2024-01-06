from pydantic import BaseModel,Field
from uuid import uuid4
from typing import Annotated,Union
from enum import Enum
from datetime import datetime

class Status (str,Enum):
    finished=True
    not_finished=False

class Gender(str,Enum):
    Male="male"
    female="female"
    
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
