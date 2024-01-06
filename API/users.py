from fastapi import APIRouter,Path,Query
from models import User
from typing import Annotated,Union
from db.db import Users,session
from sqlalchemy.orm import Session
users=APIRouter()
users_details=[]

@users.post("/users/{user_name}")
async def add_users(
    user_name:Annotated[str,Path(...,title="user_name",description="username for each user")],
    first_name:Annotated[str,Query(max_length=20,title="Enter the first name")],
    last_name:Annotated[str,Query(...,max_length=20,title="Enter the last name")],
    middle_name:Annotated[str,None]=None,
    ):
    data=User(user_name=user_name,first_name=first_name,middle_name=middle_name,last_name=last_name)
    try:
        add_user_db(data=data,ses=session)
        return {"status":"successfull"}
    except Exception as e:
        return (f"{e}")
    
# @users.get("/users/{user_name}")
# async def get_user(
#     user_name:Annotated[str,Path(...,description="give username")]
#     ):
#     try:
#         get_user_db(user_name=user_name,ses=session)
#     except Exception as e:
#         return (f"{e}")





    
def add_user_db(data:User,ses:Session):
    new_user = Users(
        user_name=data.user_name,
        first_name=data.first_name,
        last_name=data.last_name,
        middle_name=data.middle_name
    )
    ses.add(new_user)
    ses.commit()
    return True


@users.get("/users",tags=['users'])
async def list_users():
    return users_details