from sqlalchemy.orm import Session
from ..models.user import UserModel
from ..schemas.auth import CreateUserRequestSchema, Token
from fastapi import HTTPException, status
from .utils import authenticate_user, create_access_token, bycrpt_context,oauth2_bearer
from datetime import datetime, timedelta





def create_user(db:Session, create_user_request:CreateUserRequestSchema):

    create_user_model = UserModel(
        username=create_user_request.username,
        hashed_password = bycrpt_context.hash(create_user_request.password)
    )

    db.add(create_user_model)
    db.commit()


# Function to inniciate the authentication process

def authenticate_process(db: Session, form_data):
    user = authenticate_user(form_data.username, form_data.password, UserModel, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user."
            )
    
    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type':'bearer'}


