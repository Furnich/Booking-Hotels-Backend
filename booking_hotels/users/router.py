from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from booking_hotels.exception import (
    IncorrectEmailOrPasswordException,
    UserAlreadyExistsException,
)
from booking_hotels.users.auth import (
    authenticate_user,
    create_acces_token,
    get_password_hash,
)
from booking_hotels.users.dao import UsersDAO
from booking_hotels.users.dependencies import get_current_user
from booking_hotels.users.models import Users
from booking_hotels.users.schemas import SUserRegister

router = APIRouter(
    prefix="",
    tags=["Auth & Пользователи"]
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/auth/register")
async def register_user(user_data:SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email.lower())
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email.lower(),hashed_password=hashed_password,First_name=user_data.First_name.capitalize(), Last_name=user_data.Last_name.capitalize())


@router.post("/auth/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username,form_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_acces_token({"sub":str(user.id)})
    welcome = f'Добро пожаловать {user.First_name} {user.Last_name}'
    return {"msg":welcome ,"access_token": access_token, "token_type": "bearer"}


@router.post("/user/logout")
async def logout_user(response: Response):
    return {"msg": "Вы успешно вышли"}

@router.get("/user/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return {"First_name":current_user.First_name, "Last_name":current_user.Last_name, "Email":current_user.email, "ID":current_user.id}