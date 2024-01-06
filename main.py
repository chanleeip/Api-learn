'''
This is a task_management microservice
'''



'''
    project is to make a task-management microservice which has two models
    ->Task
            ->uuid
            ->task name
            ->status
            ->task_descriptiom
    ->User
            ->uuid
            ->firstname
            ->middlename
            ->lastname
    
'''


from fastapi import FastAPI,Query,Path
from typing import Annotated
from models.model import User
app=FastAPI()



@app.get("/")
def home_page():
    return {"Hello world":"nithinn"}

@app.get("/users/{user_id}")
# async def list_users(user_id:int=Path(...,title="user_id",description="unqiue id for each user"),first_name:Annotated[str,None,Query(max_length=20,title="Enter the first name")]=...,middle_name=Annotated[str,None],last_name:Annotated[str,None,Query(max_length=20,title="Enter the last name")]=...):
#     return (User(id=user_id,first_name=first_name,middle_name=middle_name,last_name=last_name))
def printuserid(user_id:Annotated[int,bool]):
    return user_id


