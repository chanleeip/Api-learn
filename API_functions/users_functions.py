import traceback
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User
from db import Users


def add_user_db(data:User,ses:Session,user_name:str):
    try:
        new_user = Users(
            username=user_name,
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name,
            gender=data.gender
        )
        print(new_user)
        ses.add(new_user)
        ses.commit()
        return {"status":"successfull"}
    except IntegrityError as e:
        ses.rollback()
        return {"status":"username already exists"}
    except Exception as e:
        print(traceback.format_exc()) 
        ses.rollback()
        return {"some error":e}

def get_user_db(user_name:str,ses:Session):
    data=ses.query(Users).filter(Users.username==user_name).first()
    if data:
         return  {"status":"sucessfull","data":data}
    return {"status":"No account found with this username"}


def get_all_user_db(ses:Session):
    data=ses.query(Users).all()
    return  {"status":"sucessfull","data":data}

def delete_user_db(username:str,ses:Session):
    data=ses.query(Users).filter(Users.username==username).first()
    if data:
        ses.delete(data)
        ses.commit()
        return {"status":"sucessfull"}
    return {"status":"No account found with this username"}
    
def update_user_db(ses:Session,body:User,username:str):
    print(body.gender.value)
    if username != body.username:
        new_username=ses.query(Users).filter(Users.username==body.username).first()
        if new_username is None:
            org_data=ses.query(Users).filter(Users.username==username).first()
            if org_data:
                org_data.username = body.username
                org_data.first_name = body.first_name
                org_data.middle_name = body.middle_name
                org_data.last_name = body.last_name
                org_data.gender=body.gender.value
                ses.commit()
                return {"status":"sucessfully updated username and details"}
        else:
            return {"status":"Username is taken. Try other username"}
    elif username==body.user_name:
        org_data=ses.query(Users).filter(Users.username==username).first()
        if org_data:
            org_data.first_name = body.first_name
            org_data.middle_name = body.middle_name
            org_data.last_name = body.last_name
            org_data.gender=body.gender.value
            ses.commit()
            return {"status":"updated the details"}
    return {"status":"Error"}