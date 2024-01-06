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


from fastapi import FastAPI
from  API.users import users

app=FastAPI()

users_details=[]


@app.get("/")
def home_page():
    return {"Hello world":"nithinn"}

app.include_router(users)

