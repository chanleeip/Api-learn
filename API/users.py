from typing import Annotated
from fastapi import APIRouter,Path,Query,Body
from models import User
from db import get_session
from API_functions import get_all_user_db,get_user_db,add_user_db,delete_user_db,update_user_db
users=APIRouter()

@users.post("/users/{user_name}")
def add_users(
    user_name:Annotated[str,Path(...,title="user_name",description="username for each user")],
    first_name:Annotated[str,Query(max_length=20,title="Enter the first name")],
    last_name:Annotated[str,Query(...,max_length=20,title="Enter the last name")],
    middle_name:Annotated[str,None]=None,
    ):
    data=User(user_name=user_name,first_name=first_name,middle_name=middle_name,last_name=last_name)
    data=add_user_db(data=data,ses=get_session())
    return data
    
@users.delete("/users/{user_name}")
def delete_users(
    user_name:Annotated[str,Path(...,description="delete any user")],
    ):
    data=delete_user_db(username=user_name,ses=get_session())
    return data

@users.put("/users/{user_name}")
def update_users(
    user_name:Annotated[str,Path(...,title="user_name",description="username for each user")],
    body:User=Body(...),
    ):
    data=update_user_db(username=user_name,ses=get_session(),body=body)
    return data


@users.get("/users/{user_name}")
def get_user(
    user_name:Annotated[str,Path(...,description="give username")]
    ):
    data=get_user_db(user_name=user_name,ses=get_session())
    return data

@users.get("/users")
def get_all_users():
    data=get_all_user_db(ses=get_session())
    return data

