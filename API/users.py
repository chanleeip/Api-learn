from fastapi import APIRouter,Path,Query
from models.model import User
from typing import Annotated,Union
users=APIRouter()
users_details=[]

@users.get("/users/{user_id}")
async def add_users(
    user_id:Annotated[int,Path(...,title="user_id",description="unqiue id for each user")],
    first_name:Annotated[str,Query(max_length=20,title="Enter the first name")],
    last_name:Annotated[str,Query(...,max_length=20,title="Enter the last name")],
    middle_name:Annotated[str,None]=None
    ):

    users_details.append(User(id=user_id,first_name=first_name,middle_name=middle_name,last_name=last_name).dict())
    return (users_details)


@users.get("/users/")
async def list_users():
    return users_details