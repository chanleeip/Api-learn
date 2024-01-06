from fastapi import FastAPI
from  API.users import users

''' This is a task_management microservice '''




'''Description:
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


app=FastAPI()


@app.get("/")
def home_page():
    return {"Hello world":"nithinn"}

app.include_router(users)
