from datetime import timedelta, datetime
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt, JWTError
from typing import Annotated
from fastapi import HTTPException, status, Depends
from dotenv import load_dotenv
import os

load_dotenv('.env')

SECRET_KEY:str = os.getenv("SECRET_KEY")
ALGORITHM:str = os.getenv("ALGORITHM")


bycrpt_context = CryptContext(schemes=['bcrypt'])
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def authenticate_user(username: str, password:str, UserModel,db):
    
    # Try to find a match of the user and the user in DB

    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        return False
    if not bycrpt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username : str , user_id: int, expires_delta: timedelta):
    encode = {'sub':username, 'id':user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')

        if username is None or user_id is None:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate user.')
        
        return {'username':username , 'id':user_id}
    
    except JWTError:
        raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate user.')