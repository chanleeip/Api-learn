from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User
from db import Users


def add_user_db(data:User,ses:Session):
    try:
        new_user = Users(
            user_name=data.user_name,
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name
        )
        ses.add(new_user)
        ses.commit()
        return {"status":"successfull"}
    except IntegrityError as e:
        ses.rollback()
        return {"status":"username already exists"}
    except Exception as e:
        ses.rollback()
        return {"some error":e}

def get_user_db(user_name:str,ses:Session):
    data=ses.query(Users).filter(Users.user_name==user_name).first()
    if data:
         return  {"status":"sucessfull","data":data}
    return {"status":"No account found with this username"}


def get_all_user_db(ses:Session):
    data=ses.query(Users).all()
    return  {"status":"sucessfull","data":data}