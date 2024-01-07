from typing import Annotated
from fastapi import APIRouter,Path,Query
from models import User
from db.db import init_db,get_session
from API_functions import get_all_user_db,get_user_db,add_user_db
users=APIRouter()
init_db()
@users.post("/users/{user_name}")
async def add_users(
    user_name:Annotated[str,Path(...,title="user_name",description="username for each user")],
    first_name:Annotated[str,Query(max_length=20,title="Enter the first name")],
    last_name:Annotated[str,Query(...,max_length=20,title="Enter the last name")],
    middle_name:Annotated[str,None]=None,
    ):
    data=User(user_name=user_name,first_name=first_name,middle_name=middle_name,last_name=last_name)
    data=add_user_db(data=data,ses=get_session())
    return data
    
    
@users.get("/users/{user_name}")
async def get_user(
    user_name:Annotated[str,Path(...,description="give username")]
    ):
    data=get_user_db(user_name=user_name,ses=get_session())
    return data

@users.get("/users")
async def get_all_users():
    data=get_all_user_db(ses=get_session())
    return data

