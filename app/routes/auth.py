from fastapi import APIRouter, status, Depends
from ..database.db_dependency import get_db
from ..schemas.auth import CreateUserRequestSchema, Token
from sqlalchemy.orm import Session
from ..services import auth
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

default_router = APIRouter()


@default_router.get("/", status_code=status.HTTP_200_OK)
async def root() -> dict[str,str]:
    return {"message": "Welcome to the API! Authenticate to be able to use"}


# Password hashing and unhashing

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    create_user_request: CreateUserRequestSchema,
    session : Session = Depends(get_db)):

    return auth.create_user(session,create_user_request)
    

@router.post("/token", response_model=Token)
async def login_for_acess_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_db)
    ):

    return auth.authenticate_process( session, form_data)


